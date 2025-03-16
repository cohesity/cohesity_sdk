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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UpgradeDetail(BaseModel):
    """
    Specifies the cluster upgrade details
    """ # noqa: E501
    cluster_id: Optional[StrictStr] = Field(default=None, description="Specifies cluster's id.", alias="clusterId")
    cluster_incarnation_id: Optional[StrictStr] = Field(default=None, description="Specifies cluster's incarnation id.", alias="clusterIncarnationID")
    cluster_name: Optional[StrictStr] = Field(default=None, description="Specifies cluster's name.", alias="clusterName")
    current_version: Optional[StrictStr] = Field(default=None, description="Specifies cluster's current version.", alias="currentVersion")
    pulse_task_id: Optional[StrictStr] = Field(default=None, description="Specifies the upgrade's nexus task ID.", alias="pulseTaskId")
    release_version: Optional[StrictStr] = Field(default=None, description="Specifies cluster's upgrade release version.", alias="releaseVersion")
    scheduled_time: Optional[StrictStr] = Field(default=None, description="Specifies the upgrade time for the cluster.", alias="scheduledTime")
    status: Optional[StrictStr] = Field(default=None, description="Specifies the upgrade status of the cluster.")
    __properties: ClassVar[List[str]] = ["clusterId", "clusterIncarnationID", "clusterName", "currentVersion", "pulseTaskId", "releaseVersion", "scheduledTime", "status"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['InProgress', 'UpgradeAvailable', 'UpToDate', 'Scheduled', 'Failed', 'ClusterUnreachable']):
            raise ValueError("must be one of enum values ('InProgress', 'UpgradeAvailable', 'UpToDate', 'Scheduled', 'Failed', 'ClusterUnreachable')")
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
        """Create an instance of UpgradeDetail from a JSON string"""
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
        # set to None if cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_id is None and "cluster_id" in self.model_fields_set:
            _dict['clusterId'] = None

        # set to None if cluster_incarnation_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_incarnation_id is None and "cluster_incarnation_id" in self.model_fields_set:
            _dict['clusterIncarnationID'] = None

        # set to None if cluster_name (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_name is None and "cluster_name" in self.model_fields_set:
            _dict['clusterName'] = None

        # set to None if current_version (nullable) is None
        # and model_fields_set contains the field
        if self.current_version is None and "current_version" in self.model_fields_set:
            _dict['currentVersion'] = None

        # set to None if pulse_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.pulse_task_id is None and "pulse_task_id" in self.model_fields_set:
            _dict['pulseTaskId'] = None

        # set to None if release_version (nullable) is None
        # and model_fields_set contains the field
        if self.release_version is None and "release_version" in self.model_fields_set:
            _dict['releaseVersion'] = None

        # set to None if scheduled_time (nullable) is None
        # and model_fields_set contains the field
        if self.scheduled_time is None and "scheduled_time" in self.model_fields_set:
            _dict['scheduledTime'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpgradeDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterId": obj.get("clusterId"),
            "clusterIncarnationID": obj.get("clusterIncarnationID"),
            "clusterName": obj.get("clusterName"),
            "currentVersion": obj.get("currentVersion"),
            "pulseTaskId": obj.get("pulseTaskId"),
            "releaseVersion": obj.get("releaseVersion"),
            "scheduledTime": obj.get("scheduledTime"),
            "status": obj.get("status")
        })
        return _obj


