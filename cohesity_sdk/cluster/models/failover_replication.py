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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class FailoverReplication(BaseModel):
    """
    Specifies the details of a failover replication.
    """ # noqa: E501
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the replication complete time in micro seconds.", alias="endTimeUsecs")
    error_message: Optional[StrictStr] = Field(default=None, description="Specifies the error details if replication status is 'Failed'.", alias="errorMessage")
    id: Optional[StrictStr] = Field(default=None, description="Specifies the replication id.")
    logical_bytes_transferred: Optional[StrictInt] = Field(default=None, description="Specifies the number of logical bytes transferred for this replication so far. This value can never exceed the total logical size of the replicated view.", alias="logicalBytesTransferred")
    logical_size_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the total amount of logical data to be transferred for this replication.", alias="logicalSizeBytes")
    percentage_completed: Optional[StrictInt] = Field(default=None, description="Specifies the percentage completed in the replication.", alias="percentageCompleted")
    physical_bytes_transferred: Optional[StrictInt] = Field(default=None, description="Specifies the number of bytes sent over the wire for this replication so far.", alias="physicalBytesTransferred")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the replication start time in micro seconds.", alias="startTimeUsecs")
    status: Optional[StrictStr] = Field(default=None, description="Specifies the replication status.")
    target_cluster_id: Optional[StrictInt] = Field(default=None, description="Specifies the failover target cluster id.", alias="targetClusterId")
    target_cluster_incarnation_id: Optional[StrictInt] = Field(default=None, description="Specifies the failover target cluster incarnation id.", alias="targetClusterIncarnationId")
    target_cluster_name: Optional[StrictStr] = Field(default=None, description="Specifies the failover target cluster name.", alias="targetClusterName")
    __properties: ClassVar[List[str]] = ["endTimeUsecs", "errorMessage", "id", "logicalBytesTransferred", "logicalSizeBytes", "percentageCompleted", "physicalBytesTransferred", "startTimeUsecs", "status", "targetClusterId", "targetClusterIncarnationId", "targetClusterName"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Running', 'Succeeded', 'Failed']):
            raise ValueError("must be one of enum values ('Running', 'Succeeded', 'Failed')")
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
        """Create an instance of FailoverReplication from a JSON string"""
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
        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['errorMessage'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if logical_bytes_transferred (nullable) is None
        # and model_fields_set contains the field
        if self.logical_bytes_transferred is None and "logical_bytes_transferred" in self.model_fields_set:
            _dict['logicalBytesTransferred'] = None

        # set to None if logical_size_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.logical_size_bytes is None and "logical_size_bytes" in self.model_fields_set:
            _dict['logicalSizeBytes'] = None

        # set to None if percentage_completed (nullable) is None
        # and model_fields_set contains the field
        if self.percentage_completed is None and "percentage_completed" in self.model_fields_set:
            _dict['percentageCompleted'] = None

        # set to None if physical_bytes_transferred (nullable) is None
        # and model_fields_set contains the field
        if self.physical_bytes_transferred is None and "physical_bytes_transferred" in self.model_fields_set:
            _dict['physicalBytesTransferred'] = None

        # set to None if start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_usecs is None and "start_time_usecs" in self.model_fields_set:
            _dict['startTimeUsecs'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if target_cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.target_cluster_id is None and "target_cluster_id" in self.model_fields_set:
            _dict['targetClusterId'] = None

        # set to None if target_cluster_incarnation_id (nullable) is None
        # and model_fields_set contains the field
        if self.target_cluster_incarnation_id is None and "target_cluster_incarnation_id" in self.model_fields_set:
            _dict['targetClusterIncarnationId'] = None

        # set to None if target_cluster_name (nullable) is None
        # and model_fields_set contains the field
        if self.target_cluster_name is None and "target_cluster_name" in self.model_fields_set:
            _dict['targetClusterName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FailoverReplication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "errorMessage": obj.get("errorMessage"),
            "id": obj.get("id"),
            "logicalBytesTransferred": obj.get("logicalBytesTransferred"),
            "logicalSizeBytes": obj.get("logicalSizeBytes"),
            "percentageCompleted": obj.get("percentageCompleted"),
            "physicalBytesTransferred": obj.get("physicalBytesTransferred"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "status": obj.get("status"),
            "targetClusterId": obj.get("targetClusterId"),
            "targetClusterIncarnationId": obj.get("targetClusterIncarnationId"),
            "targetClusterName": obj.get("targetClusterName")
        })
        return _obj


