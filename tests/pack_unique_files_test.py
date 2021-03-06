import os

from demisto_sdk.common.constants import PACKS_README_FILE_NAME
from demisto_sdk.common.hook_validations.pack_unique_files import PackUniqueFilesValidator


class TestPackUniqueFilesValidator:
    FILES_PATH = os.path.normpath(os.path.join(__file__, '..', 'test_files'))
    FAKE_PACK_PATH = os.path.join(FILES_PATH, 'fake_pack')
    FAKE_PATH_NAME = 'fake_pack'
    validator = PackUniqueFilesValidator(FAKE_PATH_NAME)
    validator.pack_path = FAKE_PACK_PATH

    def test_is_error_added(self):
        self.validator._add_error('boop')
        assert 'boop' in self.validator.get_errors(True)
        assert 'boop' in self.validator.get_errors()
        self.validator._errors = []

    def test_is_file_exist(self):
        assert self.validator._is_pack_file_exists(PACKS_README_FILE_NAME)
        assert not self.validator._is_pack_file_exists('boop')
        self.validator._errors = []

    def test_parse_file_into_list(self):
        assert ['boop', 'sade', ''] == self.validator._parse_file_into_list(PACKS_README_FILE_NAME)
        assert not self.validator._parse_file_into_list('boop')
        self.validator._errors = []

    def test_validate_pack_unique_files(self):
        assert not self.validator.validate_pack_unique_files()
        fake_validator = PackUniqueFilesValidator('fake')
        assert fake_validator.validate_pack_unique_files()
