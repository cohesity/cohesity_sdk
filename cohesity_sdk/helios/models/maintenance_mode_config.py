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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.schedule import Schedule
from cohesity_sdk.helios.models.time_range_usecs import TimeRangeUsecs
from cohesity_sdk.helios.models.workflow_intervention_spec import WorkflowInterventionSpec
from typing import Set
from typing_extensions import Self

class MaintenanceModeConfig(BaseModel):
    """
    Specifies the entity metadata for maintenance mode.
    """ # noqa: E501
    activation_time_intervals: Optional[List[TimeRangeUsecs]] = Field(default=None, description="Specifies the absolute intervals where the maintenance schedule is valid, i.e. maintenance_shedule is considered only for these time ranges. (For example, if there is one time range with [now_usecs, now_usecs + 10 days], the action will be done during the maintenance_schedule for the next 10 days.)The start time must be specified. The end time can be -1 which would denote an indefinite maintenance mode.", alias="activationTimeIntervals")
    maintenance_schedule: Optional[Schedule] = Field(default=None, alias="maintenanceSchedule")
    user_message: Optional[StrictStr] = Field(default=None, description="User provided message associated with this maintenance mode.", alias="userMessage")
    workflow_intervention_spec_list: Optional[List[WorkflowInterventionSpec]] = Field(default=None, description="Specifies the type of intervention for different workflows when the source goes into maintenance mode.", alias="workflowInterventionSpecList")
    __properties: ClassVar[List[str]] = ["activationTimeIntervals", "maintenanceSchedule", "userMessage", "workflowInterventionSpecList"]

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
        """Create an instance of MaintenanceModeConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in activation_time_intervals (list)
        _items = []
        if self.activation_time_intervals:
            for _item_activation_time_intervals in self.activation_time_intervals:
                if _item_activation_time_intervals:
                    _items.append(_item_activation_time_intervals.to_dict())
            _dict['activationTimeIntervals'] = _items
        # override the default output from pydantic by calling `to_dict()` of maintenance_schedule
        if self.maintenance_schedule:
            _dict['maintenanceSchedule'] = self.maintenance_schedule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in workflow_intervention_spec_list (list)
        _items = []
        if self.workflow_intervention_spec_list:
            for _item_workflow_intervention_spec_list in self.workflow_intervention_spec_list:
                if _item_workflow_intervention_spec_list:
                    _items.append(_item_workflow_intervention_spec_list.to_dict())
            _dict['workflowInterventionSpecList'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MaintenanceModeConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activationTimeIntervals": [TimeRangeUsecs.from_dict(_item) for _item in obj["activationTimeIntervals"]] if obj.get("activationTimeIntervals") is not None else None,
            "maintenanceSchedule": Schedule.from_dict(obj["maintenanceSchedule"]) if obj.get("maintenanceSchedule") is not None else None,
            "userMessage": obj.get("userMessage"),
            "workflowInterventionSpecList": [WorkflowInterventionSpec.from_dict(_item) for _item in obj["workflowInterventionSpecList"]] if obj.get("workflowInterventionSpecList") is not None else None
        })
        return _obj


