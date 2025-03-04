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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.models.cancellation_timeout_params import CancellationTimeoutParams
from cohesity_sdk.models.log_retention import LogRetention
from cohesity_sdk.models.retention import Retention
from cohesity_sdk.models.target_schedule import TargetSchedule
from typing import Optional, Set
from typing_extensions import Self

class CommonTargetConfiguration(BaseModel):
    """
    Specifies common parameters required while setting up additional protection target configuration.
    """ # noqa: E501
    backup_run_type: Optional[StrictStr] = Field(default=None, description="Specifies which type of run should be copied, if not set, all types of runs will be eligible for copying. If set, this will ensure that the first run of given type in the scheduled period will get copied. Currently, this can only be set to Full.", alias="backupRunType")
    config_id: Optional[StrictStr] = Field(default=None, description="Specifies the unique identifier for the target getting added. This field need to be passed only when policies are being updated.", alias="configId")
    copy_on_run_success: Optional[StrictBool] = Field(default=None, description="Specifies if Snapshots are copied from the first completely successful Protection Group Run or the first partially successful Protection Group Run occurring at the start of the replication schedule. <br> If true, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule that was completely successful i.e. Snapshots for all the Objects in the Protection Group were successfully captured. <br> If false, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule, even if first Protection Group Run was not completely successful i.e. Snapshots were not captured for all Objects in the Protection Group.", alias="copyOnRunSuccess")
    log_retention: Optional[LogRetention] = Field(default=None, alias="logRetention")
    retention: Retention
    run_timeouts: Optional[List[CancellationTimeoutParams]] = Field(default=None, description="Specifies the replication/archival timeouts for different type of runs(kFull, kRegular etc.).", alias="runTimeouts")
    schedule: TargetSchedule
    __properties: ClassVar[List[str]] = ["backupRunType", "configId", "copyOnRunSuccess", "logRetention", "retention", "runTimeouts", "schedule"]

    @field_validator('backup_run_type')
    def backup_run_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Regular', 'Full', 'Log', 'System']):
            raise ValueError("must be one of enum values ('Regular', 'Full', 'Log', 'System')")
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
        """Create an instance of CommonTargetConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of log_retention
        if self.log_retention:
            _dict['logRetention'] = self.log_retention.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retention
        if self.retention:
            _dict['retention'] = self.retention.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in run_timeouts (list)
        _items = []
        if self.run_timeouts:
            for _item_run_timeouts in self.run_timeouts:
                if _item_run_timeouts:
                    _items.append(_item_run_timeouts.to_dict())
            _dict['runTimeouts'] = _items
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # set to None if backup_run_type (nullable) is None
        # and model_fields_set contains the field
        if self.backup_run_type is None and "backup_run_type" in self.model_fields_set:
            _dict['backupRunType'] = None

        # set to None if config_id (nullable) is None
        # and model_fields_set contains the field
        if self.config_id is None and "config_id" in self.model_fields_set:
            _dict['configId'] = None

        # set to None if copy_on_run_success (nullable) is None
        # and model_fields_set contains the field
        if self.copy_on_run_success is None and "copy_on_run_success" in self.model_fields_set:
            _dict['copyOnRunSuccess'] = None

        # set to None if run_timeouts (nullable) is None
        # and model_fields_set contains the field
        if self.run_timeouts is None and "run_timeouts" in self.model_fields_set:
            _dict['runTimeouts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonTargetConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backupRunType": obj.get("backupRunType"),
            "configId": obj.get("configId"),
            "copyOnRunSuccess": obj.get("copyOnRunSuccess"),
            "logRetention": LogRetention.from_dict(obj["logRetention"]) if obj.get("logRetention") is not None else None,
            "retention": Retention.from_dict(obj["retention"]) if obj.get("retention") is not None else None,
            "runTimeouts": [CancellationTimeoutParams.from_dict(_item) for _item in obj["runTimeouts"]] if obj.get("runTimeouts") is not None else None,
            "schedule": TargetSchedule.from_dict(obj["schedule"]) if obj.get("schedule") is not None else None
        })
        return _obj


