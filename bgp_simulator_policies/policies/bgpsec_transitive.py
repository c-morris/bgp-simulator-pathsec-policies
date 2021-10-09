from copy import deepcopy

from lib_bgp_simulator import BGPRIBSPolicy, LocalRib, SendQueue, RecvQueue, Relationships

from .bgpsec import BGPsecPolicy

class BGPsecTransitivePolicy(BGPsecPolicy):

    name="BGPsec Transitive"

    def _add_ann_to_q(policy_self, self, as_obj, ann, send_rels, *args, **kwargs):
        ann_to_send = ann.copy()
        policy_self.bgpsec_transitive_modifications(self, as_obj, ann_to_send, *args, **kwargs)
        # Although this looks weird, it is correct to call the BGPsecPolicy's
        # superclass here
        super(BGPsecPolicy, policy_self)._add_ann_to_q(self, as_obj, ann_to_send, send_rels, *args, **kwargs)

    def bgpsec_transitive_modifications(policy_self, self, as_obj, ann_to_send, *args, **kwargs):
        # Set next_as for bgpsec
        ann_to_send.next_as = as_obj.asn

    def _new_ann_is_better_bgpsec(policy_self,
                                  self,
                                  current_ann,
                                  current_processed,
                                  new_ann,
                                  new_processed):
           
        # This is BGPsec Security Second, where announcements with security
        # attributes are preferred over those without, but only after
        # considering business relationships.
        current_ann_metric = policy_self._partial_path_metric(current_ann.bgpsec_path, current_ann.as_path)
        new_ann_metric = policy_self._partial_path_metric(new_ann.bgpsec_path, new_ann.as_path)
        if current_ann_metric > new_ann_metric:
            return True
        elif current_ann_metric == new_ann_metric:
            return None
        else:
            return False

    def _deep_copy_ann(policy_self, self, ann, recv_relationship, **extra_kwargs):
        """Policy modifications to ann

        When it is decided that an annoucenemnt will be saved
        in the local RIB, first it is copied with
        copy_w_sim_attrs, then this function is called (before updated
        path) then the path is updated
        """

        # Update the BGPsec path, but since attributes are transitive, the path
        # is always updated unlike BGPsec.
        kwargs = {"bgpsec_path": (self.asn, *ann.bgpsec_path)}

        kwargs.update(extra_kwargs)
        # NOTE that after this point ann has been deep copied and processed
        # This means that the AS path has 1 extra ASN that you don't need to check
        # Although this looks weird, it is correct to call the BGPsecPolicy's
        # superclass here
        return super(BGPsecPolicy, policy_self)._deep_copy_ann(self, ann, recv_relationship, **kwargs)

    def _partial_verify_path(policy_self, partial, full):
        """Verify a partial path"""
        i = 0
        j = 0
        while i < len(partial) and j < len(full):
            while partial[i] != full[j]:
                j += 1
                if j == len(full):
                    return False
            i += 1
        return i == len(partial)

    def _partial_path_metric(policy_self, partial, full):
        """Count the number of non-adopting segments"""
        i = 0
        j = 0
        switch = 0
        segments = 0
        while i < len(partial) and j < len(full):
            while partial[i] != full[j]:
                segments += switch
                switch = 0
                j += 1
                if j == len(full):
                    return segments
            switch = 1
            i += 1
            j += 1
        if j < len(full):
            segments += 1
        return segments


