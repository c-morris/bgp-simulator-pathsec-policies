from ..graphs import PGraph001
from ....attacks import IntentionalLeak
from ....policies import BGPsecAS
from ....announcements import PathManipulationAnn
from bgp_simulator_pkg import EngineTestConfig, BGPAS, ASNs


class Config001(EngineTestConfig):
    """Contains config options to run a test"""

    name = "P001"
    desc = "BGPsec security third preference test, AS 1 should prefer the path via AS 3"
    scenario = IntentionalLeak(attacker_asns={ASNs.ATTACKER.value},
                               victim_asns={ASNs.VICTIM.value},
                               BaseASCls=BGPAS,
                               AnnCls=PathManipulationAnn)
    graph = PGraph001()
    non_default_as_cls_dict = {1: BGPsecAS,
                               3: BGPsecAS,
                               4: BGPsecAS,
                               777: BGPsecAS}
    propagation_rounds = 1
