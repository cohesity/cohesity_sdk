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
from cohesity_sdk.helios.models.policy_config import PolicyConfig
from cohesity_sdk.helios.models.sla_rule import SlaRule
from cohesity_sdk.helios.models.time_of_day import TimeOfDay
from typing import Set
from typing_extensions import Self

class CommonObjectProtectParams(BaseModel):
    """
    Specifies the common parameters for object backup. These parameters are common across all types of adapters and objects.
    """ # noqa: E501
    abort_in_blackouts: Optional[StrictBool] = Field(default=None, description="Specifies whether currently executing object backup should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false.", alias="abortInBlackouts")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won't be ended.", alias="endTimeUsecs")
    policy_config: Optional[PolicyConfig] = Field(default=None, alias="policyConfig")
    policy_id: Optional[StrictStr] = Field(default=None, description="Specifies the unique id of the Protection Policy. The Policy settings will be attached with every object and will be used in backup.", alias="policyId")
    priority: Optional[StrictStr] = Field(default=None, description="Specifies the priority for the objects backup.")
    qos_policy: Optional[StrictStr] = Field(default=None, description="Specifies whether object backup will be written to HDD or SSD.", alias="qosPolicy")
    skip_rigel_for_backup: Optional[StrictBool] = Field(default=None, description="Specifies whether to skip Rigel for backup or not.", alias="skipRigelForBackup")
    sla: Optional[List[SlaRule]] = Field(default=None, description="Specifies the SLA parameters for list of objects.")
    start_time: Optional[TimeOfDay] = Field(default=None, alias="startTime")
    storage_domain_id: Optional[StrictInt] = Field(default=None, description="Specifies the Storage Domain (View Box) ID where the object backup will be taken. This is not required if Cloud archive direct is benig used.", alias="storageDomainId")
    __properties: ClassVar[List[str]] = ["abortInBlackouts", "endTimeUsecs", "policyConfig", "policyId", "priority", "qosPolicy", "skipRigelForBackup", "sla", "startTime", "storageDomainId"]

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
        """Create an instance of CommonObjectProtectParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of policy_config
        if self.policy_config:
            _dict['policyConfig'] = self.policy_config.to_dict()
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

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

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

        # set to None if skip_rigel_for_backup (nullable) is None
        # and model_fields_set contains the field
        if self.skip_rigel_for_backup is None and "skip_rigel_for_backup" in self.model_fields_set:
            _dict['skipRigelForBackup'] = None

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
        """Create an instance of CommonObjectProtectParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "abortInBlackouts": obj.get("abortInBlackouts"),
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "policyConfig": PolicyConfig.from_dict(obj["policyConfig"]) if obj.get("policyConfig") is not None else None,
            "policyId": obj.get("policyId"),
            "priority": obj.get("priority"),
            "qosPolicy": obj.get("qosPolicy"),
            "skipRigelForBackup": obj.get("skipRigelForBackup"),
            "sla": [SlaRule.from_dict(_item) for _item in obj["sla"]] if obj.get("sla") is not None else None,
            "startTime": TimeOfDay.from_dict(obj["startTime"]) if obj.get("startTime") is not None else None,
            "storageDomainId": obj.get("storageDomainId")
        })
        return _obj


