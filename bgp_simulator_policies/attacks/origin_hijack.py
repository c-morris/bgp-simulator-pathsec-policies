from lib_bgp_simulator import Prefixes, Timestamps, Relationships

from .mh_path_manipulation import MHPathManipulation


class OriginHijack(MHPathManipulation):
    """Origin hijack with a *fake* path"""

    def _get_announcements(self, **extra_ann_kwargs):
        return [self.AnnCls(prefix=Prefixes.PREFIX.value,
                            timestamp=Timestamps.VICTIM.value,
                            as_path=(self.victim_asn,),
                            # Legitimate announcement has valid BGPsec attrs
                            bgpsec_path=(self.victim_asn,),
                            next_as=self.victim_asn,
                            removed_signatures=tuple(),
                            do_communities=tuple(),
                            roa_valid_length=None,
                            roa_origin=None,
                            withdraw=False,
                            traceback_end=True,
                            seed_asn=self.victim_asn,
                            communities=tuple(),
                            recv_relationship=Relationships.ORIGIN),
                self.AnnCls(prefix=Prefixes.PREFIX.value,
                            timestamp=Timestamps.ATTACKER.value,
                            as_path=(self.attacker_asn, self.victim_asn),
                            bgpsec_path=tuple(),
                            next_as=0,
                            do_communities=tuple(),
                            roa_valid_length=None,
                            roa_origin=None,
                            withdraw=False,
                            traceback_end=True,
                            seed_asn=self.attacker_asn,
                            # Add victim to removed signatures
                            removed_signatures=(self.victim_asn,),
                            communities=tuple(),
                            recv_relationship=Relationships.ORIGIN)]
