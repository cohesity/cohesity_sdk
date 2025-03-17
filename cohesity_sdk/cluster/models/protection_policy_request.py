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
from cohesity_sdk.cluster.models.backup_policy import BackupPolicy
from cohesity_sdk.cluster.models.blackout_window import BlackoutWindow
from cohesity_sdk.cluster.models.cascaded_target_configuration import CascadedTargetConfiguration
from cohesity_sdk.cluster.models.extended_retention_policy import ExtendedRetentionPolicy
from cohesity_sdk.cluster.models.retry_options import RetryOptions
from cohesity_sdk.cluster.models.targets_configuration import TargetsConfiguration
from typing import Set
from typing_extensions import Self

class ProtectionPolicyRequest(BaseModel):
    """
    Specifies the request to create a Protection Policy.
    """ # noqa: E501
    backup_policy: BackupPolicy = Field(alias="backupPolicy")
    blackout_window: Optional[List[BlackoutWindow]] = Field(default=None, description="List of Blackout Windows. If specified, this field defines blackout periods when new Group Runs are not started. If a Group Run has been scheduled but not yet executed and the blackout period starts, the behavior depends on the policy field AbortInBlackoutPeriod.", alias="blackoutWindow")
    cascaded_targets_config: Optional[List[CascadedTargetConfiguration]] = Field(default=None, description="Specifies the configuration for cascaded replications. Using cascaded replication, replication cluster(Rx) can further replicate and archive the snapshot copies to further targets. Its recommended to create cascaded configuration where protection group will be created.", alias="cascadedTargetsConfig")
    data_lock: Optional[StrictStr] = Field(default=None, description="This field is now deprecated. Please use the DataLockConfig in the backup retention.", alias="dataLock")
    description: Optional[StrictStr] = Field(default=None, description="Specifies the description of the Protection Policy.")
    enable_smart_local_retention_adjustment: Optional[StrictBool] = Field(default=None, description="Specifies whether smart local retention adjustment is enabled or not. If enabled, local retention would be extended upon failure of any outgoing replications or archivals. Later, if manual intervention causes the failed copies to succeed, retention would automatically be reduced.", alias="enableSmartLocalRetentionAdjustment")
    extended_retention: Optional[List[ExtendedRetentionPolicy]] = Field(default=None, description="Specifies additional retention policies that should be applied to the backup snapshots. A backup snapshot will be retained up to a time that is the maximum of all retention policies that are applicable to it.", alias="extendedRetention")
    is_cbs_enabled: Optional[StrictBool] = Field(default=None, description="Specifies true if Calender Based Schedule is supported by client. Default value is assumed as false for this feature.", alias="isCBSEnabled")
    last_modification_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the last time this Policy was updated. If this is passed into a PUT request, then the backend will validate that the timestamp passed in matches the time that the policy was actually last modified. If the two timestamps do not match, then the request will be rejected with a stale error.", alias="lastModificationTimeUsecs")
    name: Optional[StrictStr] = Field(description="Specifies the name of the Protection Policy.")
    remote_target_policy: Optional[TargetsConfiguration] = Field(default=None, alias="remoteTargetPolicy")
    retry_options: Optional[RetryOptions] = Field(default=None, alias="retryOptions")
    version: Optional[StrictInt] = Field(default=None, description="Specifies the current policy verison. Policy version is incremented for optionally supporting new features and differentialting across releases.")
    template_id: Optional[StrictStr] = Field(default=None, description="Specifies the parent policy template id to which the policy is linked to.", alias="templateId")
    __properties: ClassVar[List[str]] = ["backupPolicy", "blackoutWindow", "cascadedTargetsConfig", "dataLock", "description", "enableSmartLocalRetentionAdjustment", "extendedRetention", "isCBSEnabled", "lastModificationTimeUsecs", "name", "remoteTargetPolicy", "retryOptions", "version", "templateId"]

    @field_validator('data_lock')
    def data_lock_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Compliance', 'Administrative']):
            raise ValueError("must be one of enum values ('Compliance', 'Administrative')")
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
        """Create an instance of ProtectionPolicyRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of backup_policy
        if self.backup_policy:
            _dict['backupPolicy'] = self.backup_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in blackout_window (list)
        _items = []
        if self.blackout_window:
            for _item_blackout_window in self.blackout_window:
                if _item_blackout_window:
                    _items.append(_item_blackout_window.to_dict())
            _dict['blackoutWindow'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in cascaded_targets_config (list)
        _items = []
        if self.cascaded_targets_config:
            for _item_cascaded_targets_config in self.cascaded_targets_config:
                if _item_cascaded_targets_config:
                    _items.append(_item_cascaded_targets_config.to_dict())
            _dict['cascadedTargetsConfig'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in extended_retention (list)
        _items = []
        if self.extended_retention:
            for _item_extended_retention in self.extended_retention:
                if _item_extended_retention:
                    _items.append(_item_extended_retention.to_dict())
            _dict['extendedRetention'] = _items
        # override the default output from pydantic by calling `to_dict()` of remote_target_policy
        if self.remote_target_policy:
            _dict['remoteTargetPolicy'] = self.remote_target_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retry_options
        if self.retry_options:
            _dict['retryOptions'] = self.retry_options.to_dict()
        # set to None if blackout_window (nullable) is None
        # and model_fields_set contains the field
        if self.blackout_window is None and "blackout_window" in self.model_fields_set:
            _dict['blackoutWindow'] = None

        # set to None if data_lock (nullable) is None
        # and model_fields_set contains the field
        if self.data_lock is None and "data_lock" in self.model_fields_set:
            _dict['dataLock'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if enable_smart_local_retention_adjustment (nullable) is None
        # and model_fields_set contains the field
        if self.enable_smart_local_retention_adjustment is None and "enable_smart_local_retention_adjustment" in self.model_fields_set:
            _dict['enableSmartLocalRetentionAdjustment'] = None

        # set to None if extended_retention (nullable) is None
        # and model_fields_set contains the field
        if self.extended_retention is None and "extended_retention" in self.model_fields_set:
            _dict['extendedRetention'] = None

        # set to None if is_cbs_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.is_cbs_enabled is None and "is_cbs_enabled" in self.model_fields_set:
            _dict['isCBSEnabled'] = None

        # set to None if last_modification_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_modification_time_usecs is None and "last_modification_time_usecs" in self.model_fields_set:
            _dict['lastModificationTimeUsecs'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if template_id (nullable) is None
        # and model_fields_set contains the field
        if self.template_id is None and "template_id" in self.model_fields_set:
            _dict['templateId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProtectionPolicyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backupPolicy": BackupPolicy.from_dict(obj["backupPolicy"]) if obj.get("backupPolicy") is not None else None,
            "blackoutWindow": [BlackoutWindow.from_dict(_item) for _item in obj["blackoutWindow"]] if obj.get("blackoutWindow") is not None else None,
            "cascadedTargetsConfig": [CascadedTargetConfiguration.from_dict(_item) for _item in obj["cascadedTargetsConfig"]] if obj.get("cascadedTargetsConfig") is not None else None,
            "dataLock": obj.get("dataLock"),
            "description": obj.get("description"),
            "enableSmartLocalRetentionAdjustment": obj.get("enableSmartLocalRetentionAdjustment"),
            "extendedRetention": [ExtendedRetentionPolicy.from_dict(_item) for _item in obj["extendedRetention"]] if obj.get("extendedRetention") is not None else None,
            "isCBSEnabled": obj.get("isCBSEnabled"),
            "lastModificationTimeUsecs": obj.get("lastModificationTimeUsecs"),
            "name": obj.get("name"),
            "remoteTargetPolicy": TargetsConfiguration.from_dict(obj["remoteTargetPolicy"]) if obj.get("remoteTargetPolicy") is not None else None,
            "retryOptions": RetryOptions.from_dict(obj["retryOptions"]) if obj.get("retryOptions") is not None else None,
            "version": obj.get("version"),
            "templateId": obj.get("templateId")
        })
        return _obj


