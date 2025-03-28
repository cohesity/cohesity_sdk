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
from cohesity_sdk.cluster.models.key_value_pair import KeyValuePair
from cohesity_sdk.cluster.models.protection_group_alerting_policy import ProtectionGroupAlertingPolicy
from cohesity_sdk.cluster.models.sla_rule import SlaRule
from cohesity_sdk.cluster.models.time_of_day import TimeOfDay
from typing import Set
from typing_extensions import Self

class CommonProtectionGroupRequestParams(BaseModel):
    """
    Specifies the parameters which are common between all Protection Group requests.
    """ # noqa: E501
    abort_in_blackouts: Optional[StrictBool] = Field(default=None, description="Specifies whether currently executing jobs should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. This field should not be set to true if 'pauseInBlackouts' is set to true.", alias="abortInBlackouts")
    advanced_configs: Optional[List[KeyValuePair]] = Field(default=None, description="Specifies the advanced configuration for a protection job.", alias="advancedConfigs")
    alert_policy: Optional[ProtectionGroupAlertingPolicy] = Field(default=None, alias="alertPolicy")
    description: Optional[StrictStr] = Field(default=None, description="Specifies a description of the Protection Group.")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won't be ended.", alias="endTimeUsecs")
    environment: Optional[StrictStr] = Field(description="Specifies the environment type of the Protection Group.")
    is_paused: Optional[StrictBool] = Field(default=None, description="Specifies if the the Protection Group is paused. New runs are not scheduled for the paused Protection Groups. Active run if any is not impacted.", alias="isPaused")
    last_modified_timestamp_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the last time this protection group was updated. If this is passed into a PUT request, then the backend will validate that the timestamp passed in matches the time that the protection group was actually last modified. If the two timestamps do not match, then the request will be rejected with a stale error.", alias="lastModifiedTimestampUsecs")
    name: Optional[StrictStr] = Field(description="Specifies the name of the Protection Group.")
    pause_in_blackouts: Optional[StrictBool] = Field(default=None, description="Specifies whether currently executing jobs should be paused if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. This field should not be set to true if 'abortInBlackouts' is sent as true.", alias="pauseInBlackouts")
    policy_id: Optional[StrictStr] = Field(description="Specifies the unique id of the Protection Policy associated with the Protection Group. The Policy provides retry settings Protection Schedules, Priority, SLA, etc.", alias="policyId")
    priority: Optional[StrictStr] = Field(default=None, description="Specifies the priority of the Protection Group.")
    qos_policy: Optional[StrictStr] = Field(default=None, description="Specifies whether the Protection Group will be written to HDD or SSD.", alias="qosPolicy")
    sla: Optional[List[SlaRule]] = Field(default=None, description="Specifies the SLA parameters for this Protection Group.")
    start_time: Optional[TimeOfDay] = Field(default=None, alias="startTime")
    storage_domain_id: Optional[StrictInt] = Field(default=None, description="Specifies the Storage Domain (View Box) ID where this Protection Group writes data.", alias="storageDomainId")
    __properties: ClassVar[List[str]] = ["abortInBlackouts", "advancedConfigs", "alertPolicy", "description", "endTimeUsecs", "environment", "isPaused", "lastModifiedTimestampUsecs", "name", "pauseInBlackouts", "policyId", "priority", "qosPolicy", "sla", "startTime", "storageDomainId"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kVCD', 'kAzure', 'kGCP', 'kKVM', 'kAcropolis', 'kAWS', 'kAWSNative', 'kAwsS3', 'kAWSSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSQL', 'kAzureSnapshotManager', 'kPhysical', 'kPhysicalFiles', 'kGPFS', 'kElastifile', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kPure', 'kIbmFlashSystem', 'kSQL', 'kExchange', 'kAD', 'kOracle', 'kView', 'kRemoteAdapter', 'kO365', 'kO365PublicFolders', 'kO365Teams', 'kO365Group', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kVCD', 'kAzure', 'kGCP', 'kKVM', 'kAcropolis', 'kAWS', 'kAWSNative', 'kAwsS3', 'kAWSSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSQL', 'kAzureSnapshotManager', 'kPhysical', 'kPhysicalFiles', 'kGPFS', 'kElastifile', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kPure', 'kIbmFlashSystem', 'kSQL', 'kExchange', 'kAD', 'kOracle', 'kView', 'kRemoteAdapter', 'kO365', 'kO365PublicFolders', 'kO365Teams', 'kO365Group', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc')")
        return value

    @field_validator('priority')
    def priority_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kLow', 'kMedium', 'kHigh']):
            raise ValueError("must be one of enum values ('kLow', 'kMedium', 'kHigh')")
        return value

    @field_validator('qos_policy')
    def qos_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kBackupHDD', 'kBackupSSD', 'kTestAndDevHigh', 'kBackupAll']):
            raise ValueError("must be one of enum values ('kBackupHDD', 'kBackupSSD', 'kTestAndDevHigh', 'kBackupAll')")
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
        """Create an instance of CommonProtectionGroupRequestParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in advanced_configs (list)
        _items = []
        if self.advanced_configs:
            for _item_advanced_configs in self.advanced_configs:
                if _item_advanced_configs:
                    _items.append(_item_advanced_configs.to_dict())
            _dict['advancedConfigs'] = _items
        # override the default output from pydantic by calling `to_dict()` of alert_policy
        if self.alert_policy:
            _dict['alertPolicy'] = self.alert_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sla (list)
        _items = []
        if self.sla:
            for _item_sla in self.sla:
                if _item_sla:
                    _items.append(_item_sla.to_dict())
            _dict['sla'] = _items
        # override the default output from pydantic by calling `to_dict()` of start_time
        if self.start_time:
            _dict['startTime'] = self.start_time.to_dict()
        # set to None if abort_in_blackouts (nullable) is None
        # and model_fields_set contains the field
        if self.abort_in_blackouts is None and "abort_in_blackouts" in self.model_fields_set:
            _dict['abortInBlackouts'] = None

        # set to None if advanced_configs (nullable) is None
        # and model_fields_set contains the field
        if self.advanced_configs is None and "advanced_configs" in self.model_fields_set:
            _dict['advancedConfigs'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        # set to None if is_paused (nullable) is None
        # and model_fields_set contains the field
        if self.is_paused is None and "is_paused" in self.model_fields_set:
            _dict['isPaused'] = None

        # set to None if last_modified_timestamp_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_timestamp_usecs is None and "last_modified_timestamp_usecs" in self.model_fields_set:
            _dict['lastModifiedTimestampUsecs'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if pause_in_blackouts (nullable) is None
        # and model_fields_set contains the field
        if self.pause_in_blackouts is None and "pause_in_blackouts" in self.model_fields_set:
            _dict['pauseInBlackouts'] = None

        # set to None if policy_id (nullable) is None
        # and model_fields_set contains the field
        if self.policy_id is None and "policy_id" in self.model_fields_set:
            _dict['policyId'] = None

        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict['priority'] = None

        # set to None if qos_policy (nullable) is None
        # and model_fields_set contains the field
        if self.qos_policy is None and "qos_policy" in self.model_fields_set:
            _dict['qosPolicy'] = None

        # set to None if sla (nullable) is None
        # and model_fields_set contains the field
        if self.sla is None and "sla" in self.model_fields_set:
            _dict['sla'] = None

        # set to None if storage_domain_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_id is None and "storage_domain_id" in self.model_fields_set:
            _dict['storageDomainId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonProtectionGroupRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "abortInBlackouts": obj.get("abortInBlackouts"),
            "advancedConfigs": [KeyValuePair.from_dict(_item) for _item in obj["advancedConfigs"]] if obj.get("advancedConfigs") is not None else None,
            "alertPolicy": ProtectionGroupAlertingPolicy.from_dict(obj["alertPolicy"]) if obj.get("alertPolicy") is not None else None,
            "description": obj.get("description"),
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "environment": obj.get("environment"),
            "isPaused": obj.get("isPaused"),
            "lastModifiedTimestampUsecs": obj.get("lastModifiedTimestampUsecs"),
            "name": obj.get("name"),
            "pauseInBlackouts": obj.get("pauseInBlackouts"),
            "policyId": obj.get("policyId"),
            "priority": obj.get("priority"),
            "qosPolicy": obj.get("qosPolicy"),
            "sla": [SlaRule.from_dict(_item) for _item in obj["sla"]] if obj.get("sla") is not None else None,
            "startTime": TimeOfDay.from_dict(obj["startTime"]) if obj.get("startTime") is not None else None,
            "storageDomainId": obj.get("storageDomainId")
        })
        return _obj


