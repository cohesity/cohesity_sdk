# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.oracle_archive_log_info import OracleArchiveLogInfo
from cohesity_sdk.helios.models.oracle_db_channel import OracleDbChannel
from cohesity_sdk.helios.models.oracle_recovery_validation_info import OracleRecoveryValidationInfo
from cohesity_sdk.helios.models.recover_oracle_granular_restore_info import RecoverOracleGranularRestoreInfo
from cohesity_sdk.helios.models.restore_spfile_or_pfile_info import RestoreSpfileOrPfileInfo
from cohesity_sdk.helios.models.shell_key_value_pair import ShellKeyValuePair
from typing import Optional, Set
from typing_extensions import Self

class CommonOracleAppSourceConfig(BaseModel):
    """
    Specifies a common parameters used when restoring back to original or new source.
    """ # noqa: E501
    db_channels: Optional[List[OracleDbChannel]] = Field(default=None, description="Specifies the Oracle database node channels info. If not specified, the default values assigned by the server are applied to all the databases.", alias="dbChannels")
    granular_restore_info: Optional[RecoverOracleGranularRestoreInfo] = Field(default=None, alias="granularRestoreInfo")
    oracle_archive_log_info: Optional[OracleArchiveLogInfo] = Field(default=None, alias="oracleArchiveLogInfo")
    oracle_recovery_validation_info: Optional[OracleRecoveryValidationInfo] = Field(default=None, alias="oracleRecoveryValidationInfo")
    recovery_mode: Optional[StrictBool] = Field(default=None, description="Specifies if database should be left in recovery mode.", alias="recoveryMode")
    restore_spfile_or_pfile_info: Optional[RestoreSpfileOrPfileInfo] = Field(default=None, alias="restoreSpfileOrPfileInfo")
    restore_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the time in the past to which the Oracle db needs to be restored. This allows for granular recovery of Oracle databases. If this is not set, the Oracle db will be restored from the full/incremental snapshot.", alias="restoreTimeUsecs")
    shell_evironment_vars: Optional[List[ShellKeyValuePair]] = Field(default=None, description="Specifies key value pairs of shell variables which defines the restore shell environment.", alias="shellEvironmentVars")
    use_scn_for_restore: Optional[StrictBool] = Field(default=None, description="Specifies whether database recovery performed should use scn value or not.", alias="useScnForRestore")
    __properties: ClassVar[List[str]] = ["dbChannels", "granularRestoreInfo", "oracleArchiveLogInfo", "oracleRecoveryValidationInfo", "recoveryMode", "restoreSpfileOrPfileInfo", "restoreTimeUsecs", "shellEvironmentVars", "useScnForRestore"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CommonOracleAppSourceConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in db_channels (list)
        _items = []
        if self.db_channels:
            for _item_db_channels in self.db_channels:
                if _item_db_channels:
                    _items.append(_item_db_channels.to_dict())
            _dict['dbChannels'] = _items
        # override the default output from pydantic by calling `to_dict()` of granular_restore_info
        if self.granular_restore_info:
            _dict['granularRestoreInfo'] = self.granular_restore_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oracle_archive_log_info
        if self.oracle_archive_log_info:
            _dict['oracleArchiveLogInfo'] = self.oracle_archive_log_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oracle_recovery_validation_info
        if self.oracle_recovery_validation_info:
            _dict['oracleRecoveryValidationInfo'] = self.oracle_recovery_validation_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of restore_spfile_or_pfile_info
        if self.restore_spfile_or_pfile_info:
            _dict['restoreSpfileOrPfileInfo'] = self.restore_spfile_or_pfile_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in shell_evironment_vars (list)
        _items = []
        if self.shell_evironment_vars:
            for _item_shell_evironment_vars in self.shell_evironment_vars:
                if _item_shell_evironment_vars:
                    _items.append(_item_shell_evironment_vars.to_dict())
            _dict['shellEvironmentVars'] = _items
        # set to None if db_channels (nullable) is None
        # and model_fields_set contains the field
        if self.db_channels is None and "db_channels" in self.model_fields_set:
            _dict['dbChannels'] = None

        # set to None if recovery_mode (nullable) is None
        # and model_fields_set contains the field
        if self.recovery_mode is None and "recovery_mode" in self.model_fields_set:
            _dict['recoveryMode'] = None

        # set to None if restore_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.restore_time_usecs is None and "restore_time_usecs" in self.model_fields_set:
            _dict['restoreTimeUsecs'] = None

        # set to None if shell_evironment_vars (nullable) is None
        # and model_fields_set contains the field
        if self.shell_evironment_vars is None and "shell_evironment_vars" in self.model_fields_set:
            _dict['shellEvironmentVars'] = None

        # set to None if use_scn_for_restore (nullable) is None
        # and model_fields_set contains the field
        if self.use_scn_for_restore is None and "use_scn_for_restore" in self.model_fields_set:
            _dict['useScnForRestore'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonOracleAppSourceConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dbChannels": [OracleDbChannel.from_dict(_item) for _item in obj["dbChannels"]] if obj.get("dbChannels") is not None else None,
            "granularRestoreInfo": RecoverOracleGranularRestoreInfo.from_dict(obj["granularRestoreInfo"]) if obj.get("granularRestoreInfo") is not None else None,
            "oracleArchiveLogInfo": OracleArchiveLogInfo.from_dict(obj["oracleArchiveLogInfo"]) if obj.get("oracleArchiveLogInfo") is not None else None,
            "oracleRecoveryValidationInfo": OracleRecoveryValidationInfo.from_dict(obj["oracleRecoveryValidationInfo"]) if obj.get("oracleRecoveryValidationInfo") is not None else None,
            "recoveryMode": obj.get("recoveryMode"),
            "restoreSpfileOrPfileInfo": RestoreSpfileOrPfileInfo.from_dict(obj["restoreSpfileOrPfileInfo"]) if obj.get("restoreSpfileOrPfileInfo") is not None else None,
            "restoreTimeUsecs": obj.get("restoreTimeUsecs"),
            "shellEvironmentVars": [ShellKeyValuePair.from_dict(_item) for _item in obj["shellEvironmentVars"]] if obj.get("shellEvironmentVars") is not None else None,
            "useScnForRestore": obj.get("useScnForRestore")
        })
        return _obj


