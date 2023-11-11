from ..graphs import PGraph006
from ....attacks import IntentionalLeak
from ....policies import BGPsecTransitiveAS
from ....announcements import PathManipulationAnn
from bgpy import EngineTestConfig, BGPAS, ASNs


class Config011(EngineTestConfig):
    """Contains config options to run a test"""

    name = "P011"
    desc = "Graph 6 test, BGPsec Transitive"
    scenario = IntentionalLeak(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        BaseASCls=BGPAS,
        AnnCls=PathManipulationAnn,
    )
    graph = PGraph006()
    non_default_as_cls_dict = {
        1: BGPsecTransitiveAS,
        2: BGPsecTransitiveAS,
        3: BGPsecTransitiveAS,
        4: BGPsecTransitiveAS,
        5: BGPsecTransitiveAS,
        6: BGPsecTransitiveAS,
        7: BGPsecTransitiveAS,
        8: BGPsecTransitiveAS,
        9: BGPsecTransitiveAS,
        10: BGPsecTransitiveAS,
        11: BGPsecTransitiveAS,
        12: BGPsecTransitiveAS,
        14: BGPsecTransitiveAS,
        777: BGPsecTransitiveAS,
    }
    propagation_rounds = 1