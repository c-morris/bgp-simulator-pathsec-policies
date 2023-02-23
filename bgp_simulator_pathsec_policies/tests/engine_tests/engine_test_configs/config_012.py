from ..graphs import PGraph006
from ....attacks import IntentionalLeak
from ....policies import BGPsecTransitiveDownOnlyAS
from ....announcements import PathManipulationAnn
from bgp_simulator_pkg import EngineTestConfig, BGPAS, ASNs


class Config012(EngineTestConfig):
    """Contains config options to run a test"""

    name = "P012"
    desc = "Graph 6 test, BGPsec Transitive Down Only"
    scenario = IntentionalLeak(attacker_asns={ASNs.ATTACKER.value},
                               victim_asns={ASNs.VICTIM.value},
                               BaseASCls=BGPAS,
                               AnnCls=PathManipulationAnn)
    graph = PGraph006()
    non_default_as_cls_dict = {1: BGPsecTransitiveDownOnlyAS,
                               2: BGPsecTransitiveDownOnlyAS,
                               3: BGPsecTransitiveDownOnlyAS,
                               4: BGPsecTransitiveDownOnlyAS,
                               5: BGPsecTransitiveDownOnlyAS,
                               6: BGPsecTransitiveDownOnlyAS,
                               7: BGPsecTransitiveDownOnlyAS,
                               8: BGPsecTransitiveDownOnlyAS,
                               9: BGPsecTransitiveDownOnlyAS,
                               10: BGPsecTransitiveDownOnlyAS,
                               11: BGPsecTransitiveDownOnlyAS,
                               12: BGPsecTransitiveDownOnlyAS,
                               14: BGPsecTransitiveDownOnlyAS,
                               777: BGPsecTransitiveDownOnlyAS}
    propagation_rounds = 1
