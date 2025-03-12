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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from cohesity_sdk.cluster.models.archival_target_tier_info import ArchivalTargetTierInfo
from cohesity_sdk.cluster.models.object_progress_info import ObjectProgressInfo
from cohesity_sdk.cluster.models.progress_stats import ProgressStats
from cohesity_sdk.cluster.models.progress_task_event import ProgressTaskEvent
from typing import Set
from typing_extensions import Self

class ArchivalTargetProgressInfo(BaseModel):
    """
    Specifies the progress of an archival run target.
    """ # noqa: E501
    archival_task_id: Optional[StrictStr] = Field(default=None, description="Specifies the archival task id. This is a protection group UID which only applies when archival type is 'Tape'.", alias="archivalTaskId")
    ownership_context: Optional[StrictStr] = Field(default=None, description="Specifies the ownership context for the target.", alias="ownershipContext")
    target_id: Optional[StrictInt] = Field(default=None, description="Specifies the archival target ID.", alias="targetId")
    target_name: Optional[StrictStr] = Field(default=None, description="Specifies the archival target name.", alias="targetName")
    target_type: Optional[StrictStr] = Field(default=None, description="Specifies the archival target type.", alias="targetType")
    tier_settings: Optional[ArchivalTargetTierInfo] = Field(default=None, alias="tierSettings")
    usage_type: Optional[StrictStr] = Field(default=None, description="Specifies the usage type for the target.", alias="usageType")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time of the progress task in Unix epoch Timestamp(in microseconds).", alias="endTimeUsecs")
    events: Optional[List[ProgressTaskEvent]] = Field(default=None, description="Specifies the event log created for progress Task.")
    expected_remaining_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the expected remaining time of the progress task in Unix epoch Timestamp(in microseconds).", alias="expectedRemainingTimeUsecs")
    percentage_completed: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Specifies the current completed percentage of the progress task.", alias="percentageCompleted")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of the progress task in Unix epoch Timestamp(in microseconds).", alias="startTimeUsecs")
    stats: Optional[ProgressStats] = None
    status: Optional[StrictStr] = Field(default=None, description="Specifies the current status of the progress task.")
    objects: Optional[List[ObjectProgressInfo]] = Field(default=None, description="Specifies progress for objects.")
    __properties: ClassVar[List[str]] = ["archivalTaskId", "ownershipContext", "targetId", "targetName", "targetType", "tierSettings", "usageType", "endTimeUsecs", "events", "expectedRemainingTimeUsecs", "percentageCompleted", "startTimeUsecs", "stats", "status", "objects"]

    @field_validator('ownership_context')
    def ownership_context_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Local', 'FortKnox']):
            raise ValueError("must be one of enum values ('Local', 'FortKnox')")
        return value

    @field_validator('target_type')
    def target_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Tape', 'Cloud', 'Nas']):
            raise ValueError("must be one of enum values ('Tape', 'Cloud', 'Nas')")
        return value

    @field_validator('usage_type')
    def usage_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Archival', 'Tiering', 'Rpaas']):
            raise ValueError("must be one of enum values ('Archival', 'Tiering', 'Rpaas')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Active', 'Finished', 'FinishedWithError', 'Canceled', 'FinishedGarbageCollected']):
            raise ValueError("must be one of enum values ('Active', 'Finished', 'FinishedWithError', 'Canceled', 'FinishedGarbageCollected')")
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
        """Create an instance of ArchivalTargetProgressInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tier_settings
        if self.tier_settings:
            _dict['tierSettings'] = self.tier_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item_events in self.events:
                if _item_events:
                    _items.append(_item_events.to_dict())
            _dict['events'] = _items
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # set to None if archival_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.archival_task_id is None and "archival_task_id" in self.model_fields_set:
            _dict['archivalTaskId'] = None

        # set to None if ownership_context (nullable) is None
        # and model_fields_set contains the field
        if self.ownership_context is None and "ownership_context" in self.model_fields_set:
            _dict['ownershipContext'] = None

        # set to None if target_id (nullable) is None
        # and model_fields_set contains the field
        if self.target_id is None and "target_id" in self.model_fields_set:
            _dict['targetId'] = None

        # set to None if target_name (nullable) is None
        # and model_fields_set contains the field
        if self.target_name is None and "target_name" in self.model_fields_set:
            _dict['targetName'] = None

        # set to None if target_type (nullable) is None
        # and model_fields_set contains the field
        if self.target_type is None and "target_type" in self.model_fields_set:
            _dict['targetType'] = None

        # set to None if usage_type (nullable) is None
        # and model_fields_set contains the field
        if self.usage_type is None and "usage_type" in self.model_fields_set:
            _dict['usageType'] = None

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if expected_remaining_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.expected_remaining_time_usecs is None and "expected_remaining_time_usecs" in self.model_fields_set:
            _dict['expectedRemainingTimeUsecs'] = None

        # set to None if percentage_completed (nullable) is None
        # and model_fields_set contains the field
        if self.percentage_completed is None and "percentage_completed" in self.model_fields_set:
            _dict['percentageCompleted'] = None

        # set to None if start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_usecs is None and "start_time_usecs" in self.model_fields_set:
            _dict['startTimeUsecs'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if objects (nullable) is None
        # and model_fields_set contains the field
        if self.objects is None and "objects" in self.model_fields_set:
            _dict['objects'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ArchivalTargetProgressInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivalTaskId": obj.get("archivalTaskId"),
            "ownershipContext": obj.get("ownershipContext"),
            "targetId": obj.get("targetId"),
            "targetName": obj.get("targetName"),
            "targetType": obj.get("targetType"),
            "tierSettings": ArchivalTargetTierInfo.from_dict(obj["tierSettings"]) if obj.get("tierSettings") is not None else None,
            "usageType": obj.get("usageType"),
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "events": [ProgressTaskEvent.from_dict(_item) for _item in obj["events"]] if obj.get("events") is not None else None,
            "expectedRemainingTimeUsecs": obj.get("expectedRemainingTimeUsecs"),
            "percentageCompleted": obj.get("percentageCompleted"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "stats": ProgressStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "status": obj.get("status"),
            "objects": [ObjectProgressInfo.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None
        })
        return _obj


