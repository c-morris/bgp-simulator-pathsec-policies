from ..graphs import PGraph005
from ....attacks import IntentionalLeak
from ....policies import BGPsecAS
from ....announcements import PathManipulationAnn
from bgpy import EngineTestConfig, BGPAS, ASNs


class Config007(EngineTestConfig):
    """Contains config options to run a test"""

    name = "P007"
    desc = "Small Graph test, BGPsec"
    scenario = IntentionalLeak(
        attacker_asns={ASNs.ATTACKER.value},
        victim_asns={ASNs.VICTIM.value},
        BaseASCls=BGPAS,
        AnnCls=PathManipulationAnn,
    )
    graph = PGraph005()
    non_default_as_cls_dict = {
        1: BGPsecAS,
        2: BGPsecAS,
        3: BGPsecAS,
        4: BGPsecAS,
        5: BGPsecAS,
        6: BGPsecAS,
        7: BGPsecAS,
        8: BGPsecAS,
        9: BGPsecAS,
        10: BGPsecAS,
        11: BGPsecAS,
        12: BGPsecAS,
        14: BGPsecAS,
        777: BGPsecAS,
    }
    propagation_rounds = 1