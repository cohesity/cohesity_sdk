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
from cohesity_sdk.helios.models.object_string_identifier import ObjectStringIdentifier
from cohesity_sdk.helios.models.progress_stats import ProgressStats
from cohesity_sdk.helios.models.progress_task_event import ProgressTaskEvent
from cohesity_sdk.helios.models.progress_task_info import ProgressTaskInfo
from typing import Set
from typing_extensions import Self

class ObjectProgressInfo(BaseModel):
    """
    Specifies the progress of an object.
    """ # noqa: E501
    entity_id: Optional[ObjectStringIdentifier] = Field(default=None, alias="entityId")
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the environment of the object.")
    id: Optional[StrictInt] = Field(default=None, description="Specifies object id.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the object.")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies registered source id to which object belongs.", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies registered source name to which object belongs.", alias="sourceName")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time of the progress task in Unix epoch Timestamp(in microseconds).", alias="endTimeUsecs")
    events: Optional[List[ProgressTaskEvent]] = Field(default=None, description="Specifies the event log created for progress Task.")
    expected_remaining_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the expected remaining time of the progress task in Unix epoch Timestamp(in microseconds).", alias="expectedRemainingTimeUsecs")
    percentage_completed: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Specifies the current completed percentage of the progress task.", alias="percentageCompleted")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of the progress task in Unix epoch Timestamp(in microseconds).", alias="startTimeUsecs")
    stats: Optional[ProgressStats] = None
    status: Optional[StrictStr] = Field(default=None, description="Specifies the current status of the progress task.")
    failed_attempts: Optional[List[ProgressTaskInfo]] = Field(default=None, description="Specifies progress for failed attempts of this object.", alias="failedAttempts")
    __properties: ClassVar[List[str]] = ["entityId", "environment", "id", "name", "sourceId", "sourceName", "endTimeUsecs", "events", "expectedRemainingTimeUsecs", "percentageCompleted", "startTimeUsecs", "stats", "status", "failedAttempts"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc')")
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
        """Create an instance of ObjectProgressInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of entity_id
        if self.entity_id:
            _dict['entityId'] = self.entity_id.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of each item in failed_attempts (list)
        _items = []
        if self.failed_attempts:
            for _item_failed_attempts in self.failed_attempts:
                if _item_failed_attempts:
                    _items.append(_item_failed_attempts.to_dict())
            _dict['failedAttempts'] = _items
        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        # set to None if source_name (nullable) is None
        # and model_fields_set contains the field
        if self.source_name is None and "source_name" in self.model_fields_set:
            _dict['sourceName'] = None

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

        # set to None if failed_attempts (nullable) is None
        # and model_fields_set contains the field
        if self.failed_attempts is None and "failed_attempts" in self.model_fields_set:
            _dict['failedAttempts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectProgressInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entityId": ObjectStringIdentifier.from_dict(obj["entityId"]) if obj.get("entityId") is not None else None,
            "environment": obj.get("environment"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName"),
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "events": [ProgressTaskEvent.from_dict(_item) for _item in obj["events"]] if obj.get("events") is not None else None,
            "expectedRemainingTimeUsecs": obj.get("expectedRemainingTimeUsecs"),
            "percentageCompleted": obj.get("percentageCompleted"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "stats": ProgressStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "status": obj.get("status"),
            "failedAttempts": [ProgressTaskInfo.from_dict(_item) for _item in obj["failedAttempts"]] if obj.get("failedAttempts") is not None else None
        })
        return _obj


