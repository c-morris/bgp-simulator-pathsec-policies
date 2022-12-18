import random
from typing import List, Optional

from bgp_simulator_pkg import BGPAS


class TransitiveDroppingAS(BGPAS):
    """Drops transitive attributes with some probability""" 
    name = "TransitiveDroppingAS"

    def __init__(self,
                 *args,
                 transitive_dropping_percent=1.0,
                 **kwargs):
        # Set the probability of dropping transitive attrs for *this* AS only
        # TODO make this more uniform random
        self.transitive_dropping = (
            random.random() < (transitive_dropping_percent / 100.0))

        super(TransitiveDroppingAS, self).__init__(*args,
                                                   **kwargs)
    def _process_outgoing_ann(self, as_obj, ann, propagate_to, send_rels, *args, **kwargs): # noqa E501
        """If this is a transitive dropping AS, drop the transitive attributes"""
        ann_to_send = ann.copy()
        if self.transitive_dropping:
            ann_to_send.next_as = 0
            ann_to_send.do_communities = tuple()
            # The signatures removed, if any, will be detected by adopting ASes
            ann_to_send.removed_signatures = ann_to_send.bgpsec_path
            ann_to_send.bgpsec_path = tuple()
        super(TransitiveDroppingAS, self)._process_outgoing_ann(as_obj, ann_to_send, propagate_to, send_rels, *args, **kwargs) # noqa E501


