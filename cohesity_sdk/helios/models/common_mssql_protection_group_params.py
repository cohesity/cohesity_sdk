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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.advanced_settings import AdvancedSettings
from cohesity_sdk.helios.models.filter import Filter
from cohesity_sdk.helios.models.pre_post_script_params import PrePostScriptParams
from typing import Optional, Set
from typing_extensions import Self

class CommonMSSQLProtectionGroupParams(BaseModel):
    """
    Specifies the common params to create a MSSQL Protection Group.
    """ # noqa: E501
    aag_backup_preference_type: Optional[StrictStr] = Field(default=None, description="Specifies the preference type for backing up databases that are part of an AAG. If not specified, then default preferences of the AAG server are applied. This field wont be applicable if user DB preference is set to skip AAG databases.", alias="aagBackupPreferenceType")
    advanced_settings: Optional[AdvancedSettings] = Field(default=None, alias="advancedSettings")
    backup_system_dbs: Optional[StrictBool] = Field(default=None, description="Specifies whether to backup system databases. If not specified then parameter is set to true.", alias="backupSystemDbs")
    exclude_filters: Optional[List[Filter]] = Field(default=None, description="Specifies the list of exclusion filters applied during the group creation or edit. These exclusion filters can be wildcard supported strings or regular expressions. Objects satisfying the will filters will be excluded during backup and also auto protected objects will be ignored if filtered by any of the filters.", alias="excludeFilters")
    full_backups_copy_only: Optional[StrictBool] = Field(default=None, description="Specifies whether full backups should be copy-only.", alias="fullBackupsCopyOnly")
    log_backup_num_streams: Optional[StrictInt] = Field(default=None, description="Specifies the number of streams to be used for log backups.", alias="logBackupNumStreams")
    log_backup_with_clause: Optional[StrictStr] = Field(default=None, description="Specifies the WithClause to be used for log backups.", alias="logBackupWithClause")
    pre_post_script: Optional[PrePostScriptParams] = Field(default=None, alias="prePostScript")
    use_aag_preferences_from_server: Optional[StrictBool] = Field(default=None, description="Specifies whether or not the AAG backup preferences specified on the SQL Server host should be used.", alias="useAagPreferencesFromServer")
    user_db_backup_preference_type: Optional[StrictStr] = Field(default=None, description="Specifies the preference type for backing up user databases on the host.", alias="userDbBackupPreferenceType")
    __properties: ClassVar[List[str]] = ["aagBackupPreferenceType", "advancedSettings", "backupSystemDbs", "excludeFilters", "fullBackupsCopyOnly", "logBackupNumStreams", "logBackupWithClause", "prePostScript", "useAagPreferencesFromServer", "userDbBackupPreferenceType"]

    @field_validator('aag_backup_preference_type')
    def aag_backup_preference_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kPrimaryReplicaOnly', 'kSecondaryReplicaOnly', 'kPreferSecondaryReplica', 'kAnyReplica']):
            raise ValueError("must be one of enum values ('kPrimaryReplicaOnly', 'kSecondaryReplicaOnly', 'kPreferSecondaryReplica', 'kAnyReplica')")
        return value

    @field_validator('user_db_backup_preference_type')
    def user_db_backup_preference_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kBackupAllDatabases', 'kBackupAllExceptAAGDatabases', 'kBackupOnlyAAGDatabases']):
            raise ValueError("must be one of enum values ('kBackupAllDatabases', 'kBackupAllExceptAAGDatabases', 'kBackupOnlyAAGDatabases')")
        return value

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
        """Create an instance of CommonMSSQLProtectionGroupParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of advanced_settings
        if self.advanced_settings:
            _dict['advancedSettings'] = self.advanced_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in exclude_filters (list)
        _items = []
        if self.exclude_filters:
            for _item_exclude_filters in self.exclude_filters:
                if _item_exclude_filters:
                    _items.append(_item_exclude_filters.to_dict())
            _dict['excludeFilters'] = _items
        # override the default output from pydantic by calling `to_dict()` of pre_post_script
        if self.pre_post_script:
            _dict['prePostScript'] = self.pre_post_script.to_dict()
        # set to None if aag_backup_preference_type (nullable) is None
        # and model_fields_set contains the field
        if self.aag_backup_preference_type is None and "aag_backup_preference_type" in self.model_fields_set:
            _dict['aagBackupPreferenceType'] = None

        # set to None if backup_system_dbs (nullable) is None
        # and model_fields_set contains the field
        if self.backup_system_dbs is None and "backup_system_dbs" in self.model_fields_set:
            _dict['backupSystemDbs'] = None

        # set to None if exclude_filters (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_filters is None and "exclude_filters" in self.model_fields_set:
            _dict['excludeFilters'] = None

        # set to None if full_backups_copy_only (nullable) is None
        # and model_fields_set contains the field
        if self.full_backups_copy_only is None and "full_backups_copy_only" in self.model_fields_set:
            _dict['fullBackupsCopyOnly'] = None

        # set to None if log_backup_num_streams (nullable) is None
        # and model_fields_set contains the field
        if self.log_backup_num_streams is None and "log_backup_num_streams" in self.model_fields_set:
            _dict['logBackupNumStreams'] = None

        # set to None if log_backup_with_clause (nullable) is None
        # and model_fields_set contains the field
        if self.log_backup_with_clause is None and "log_backup_with_clause" in self.model_fields_set:
            _dict['logBackupWithClause'] = None

        # set to None if use_aag_preferences_from_server (nullable) is None
        # and model_fields_set contains the field
        if self.use_aag_preferences_from_server is None and "use_aag_preferences_from_server" in self.model_fields_set:
            _dict['useAagPreferencesFromServer'] = None

        # set to None if user_db_backup_preference_type (nullable) is None
        # and model_fields_set contains the field
        if self.user_db_backup_preference_type is None and "user_db_backup_preference_type" in self.model_fields_set:
            _dict['userDbBackupPreferenceType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonMSSQLProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aagBackupPreferenceType": obj.get("aagBackupPreferenceType"),
            "advancedSettings": AdvancedSettings.from_dict(obj["advancedSettings"]) if obj.get("advancedSettings") is not None else None,
            "backupSystemDbs": obj.get("backupSystemDbs"),
            "excludeFilters": [Filter.from_dict(_item) for _item in obj["excludeFilters"]] if obj.get("excludeFilters") is not None else None,
            "fullBackupsCopyOnly": obj.get("fullBackupsCopyOnly"),
            "logBackupNumStreams": obj.get("logBackupNumStreams"),
            "logBackupWithClause": obj.get("logBackupWithClause"),
            "prePostScript": PrePostScriptParams.from_dict(obj["prePostScript"]) if obj.get("prePostScript") is not None else None,
            "useAagPreferencesFromServer": obj.get("useAagPreferencesFromServer"),
            "userDbBackupPreferenceType": obj.get("userDbBackupPreferenceType")
        })
        return _obj


