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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class CreateCloudRetrieveTaskRequest(BaseModel):
    """
    Specifies create cloud retrieve task request parameters.
    """ # noqa: E501
    cluster_id: Optional[StrictInt] = Field(default=None, description="Specifies the cluster ID.", alias="clusterId")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time in microseconds and filter the tasks by the end time.", alias="endTimeUsecs")
    job_ids: Optional[List[StrictStr]] = Field(default=None, description="Job ids to retrieve.", alias="jobIds")
    retrieve_all_jobs: Optional[StrictBool] = Field(default=None, description="Specifies whether to retrieve all tasks.", alias="retrieveAllJobs")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time in microseconds and filter the task by the start time.", alias="startTimeUsecs")
    vault_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the array of vault IDs.", alias="vaultIds")
    __properties: ClassVar[List[str]] = ["clusterId", "endTimeUsecs", "jobIds", "retrieveAllJobs", "startTimeUsecs", "vaultIds"]

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
        """Create an instance of CreateCloudRetrieveTaskRequest from a JSON string"""
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

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if job_ids (nullable) is None
        # and model_fields_set contains the field
        if self.job_ids is None and "job_ids" in self.model_fields_set:
            _dict['jobIds'] = None

        # set to None if retrieve_all_jobs (nullable) is None
        # and model_fields_set contains the field
        if self.retrieve_all_jobs is None and "retrieve_all_jobs" in self.model_fields_set:
            _dict['retrieveAllJobs'] = None

        # set to None if start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_usecs is None and "start_time_usecs" in self.model_fields_set:
            _dict['startTimeUsecs'] = None

        # set to None if vault_ids (nullable) is None
        # and model_fields_set contains the field
        if self.vault_ids is None and "vault_ids" in self.model_fields_set:
            _dict['vaultIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateCloudRetrieveTaskRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterId": obj.get("clusterId"),
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "jobIds": obj.get("jobIds"),
            "retrieveAllJobs": obj.get("retrieveAllJobs"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "vaultIds": obj.get("vaultIds")
        })
        return _obj


