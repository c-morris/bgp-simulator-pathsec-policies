from ..graphs import PGraph009
from ....attacks import Eavesdropper
from ....policies import BGPsecTransitiveDownOnlyEncrUpAS
from ....announcements import PathManipulationAnn
from ....subgraphs import OverheadBPOAllSubgraph
from bgpy import EngineTestConfig, ASNs, BGPAS


class Config035(EngineTestConfig):
    """Contains config options to run a test"""

    name = "P035"
    desc = "GlobalEavesdropper with Encrypted UP attributes test"
    scenario = Eavesdropper(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        BaseASCls=BGPAS,
        AdoptASCls=BGPsecTransitiveDownOnlyEncrUpAS,  # noqa E501
        AnnCls=PathManipulationAnn,
        no_hash=False,
    )
    graph = PGraph009()
    non_default_as_cls_dict = {
        1: BGPsecTransitiveDownOnlyEncrUpAS,
        3: BGPsecTransitiveDownOnlyEncrUpAS,
        4: BGPsecTransitiveDownOnlyEncrUpAS,
        5: BGPsecTransitiveDownOnlyEncrUpAS,
        7: BGPsecTransitiveDownOnlyEncrUpAS,
        777: BGPsecTransitiveDownOnlyEncrUpAS,
    }
    propagation_rounds = 2
    SubgraphCls = OverheadBPOAllSubgraph