import unittest

from pybambu.bambu_client import BambuClient


class TestHideAmsFirmwareMismatchOption(unittest.TestCase):
    """Config entries created before the option existed carry no value for it, so the
    default is what every existing install gets."""

    def test_defaults_to_shown(self):
        client = BambuClient({'host': '192.0.2.10', 'serial': 'TESTSERIAL123', 'enable_camera': False})

        self.assertFalse(client.hide_ams_firmware_mismatch)

    def test_can_be_turned_on(self):
        client = BambuClient({
            'host': '192.0.2.10',
            'serial': 'TESTSERIAL123',
            'enable_camera': False,
            'hide_ams_firmware_mismatch': True,
        })

        self.assertTrue(client.hide_ams_firmware_mismatch)
