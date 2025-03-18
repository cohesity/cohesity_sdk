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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.helios_cloud_spin_target import HeliosCloudSpinTarget
from cohesity_sdk.helios.models.helios_retention import HeliosRetention
from cohesity_sdk.helios.models.helios_target_schedule import HeliosTargetSchedule
from typing import Set
from typing_extensions import Self

class HeliosCloudSpinConfig(BaseModel):
    """
    Specifies settings for copying Snapshots to on prem.
    """ # noqa: E501
    config_id: Optional[StrictStr] = Field(default=None, description="Specifies the unique identifier for the target getting added. This field need to be passed only when helios policies are updated.", alias="configId")
    copy_on_run_success: Optional[StrictBool] = Field(default=None, description="Specifies if Snapshots are copied from the first completely successful Protection Group Run or the first partially successful Protection Group Run occurring at the start of the replication schedule. <br> If true, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule that was completely successful i.e. Snapshots for all the Objects in the Protection Group were successfully captured. <br> If false, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule, even if first Protection Group Run was not completely successful i.e. Snapshots were not captured for all Objects in the Protection Group.", alias="copyOnRunSuccess")
    retention: Optional[HeliosRetention] = None
    schedule: Optional[HeliosTargetSchedule] = None
    target: HeliosCloudSpinTarget
    __properties: ClassVar[List[str]] = ["configId", "copyOnRunSuccess", "retention", "schedule", "target"]

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
        """Create an instance of HeliosCloudSpinConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of retention
        if self.retention:
            _dict['retention'] = self.retention.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # set to None if config_id (nullable) is None
        # and model_fields_set contains the field
        if self.config_id is None and "config_id" in self.model_fields_set:
            _dict['configId'] = None

        # set to None if copy_on_run_success (nullable) is None
        # and model_fields_set contains the field
        if self.copy_on_run_success is None and "copy_on_run_success" in self.model_fields_set:
            _dict['copyOnRunSuccess'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosCloudSpinConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configId": obj.get("configId"),
            "copyOnRunSuccess": obj.get("copyOnRunSuccess"),
            "retention": HeliosRetention.from_dict(obj["retention"]) if obj.get("retention") is not None else None,
            "schedule": HeliosTargetSchedule.from_dict(obj["schedule"]) if obj.get("schedule") is not None else None,
            "target": HeliosCloudSpinTarget.from_dict(obj["target"]) if obj.get("target") is not None else None
        })
        return _obj


