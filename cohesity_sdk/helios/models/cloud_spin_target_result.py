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
from cohesity_sdk.helios.models.aws_cloud_spin_params import AwsCloudSpinParams
from cohesity_sdk.helios.models.azure_cloud_spin_params import AzureCloudSpinParams
from cohesity_sdk.helios.models.cloud_spin_data_stats import CloudSpinDataStats
from cohesity_sdk.helios.models.data_lock_constraints import DataLockConstraints
from typing import Optional, Set
from typing_extensions import Self

class CloudSpinTargetResult(BaseModel):
    """
    Cloud Spin result for a target.
    """ # noqa: E501
    aws_params: Optional[AwsCloudSpinParams] = Field(default=None, alias="awsParams")
    azure_params: Optional[AzureCloudSpinParams] = Field(default=None, alias="azureParams")
    id: Optional[StrictInt] = Field(default=None, description="Specifies the unique id of the cloud spin entity.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the already added cloud spin target.")
    cloudspin_task_id: Optional[StrictStr] = Field(default=None, description="Task ID for a CloudSpin protection run.", alias="cloudspinTaskId")
    data_lock_constraints: Optional[DataLockConstraints] = Field(default=None, alias="dataLockConstraints")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time of Cloud Spin in Unix epoch Timestamp(in microseconds) for a target.", alias="endTimeUsecs")
    expiry_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the expiry time of attempt in Unix epoch Timestamp (in microseconds) for an object.", alias="expiryTimeUsecs")
    is_manually_deleted: Optional[StrictBool] = Field(default=None, description="Specifies whether the snapshot is deleted manually.", alias="isManuallyDeleted")
    message: Optional[StrictStr] = Field(default=None, description="Message about the Cloud Spin run.")
    on_legal_hold: Optional[StrictBool] = Field(default=None, description="Specifies the legal hold status for a cloud spin target.", alias="onLegalHold")
    progress_task_id: Optional[StrictStr] = Field(default=None, description="Progress monitor task id for Cloud Spin run.", alias="progressTaskId")
    start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of Cloud Spin in Unix epoch Timestamp(in microseconds) for a target.", alias="startTimeUsecs")
    stats: Optional[CloudSpinDataStats] = None
    status: Optional[StrictStr] = Field(default=None, description="Status of the Cloud Spin for a target. 'Running' indicates that the run is still running. 'Canceled' indicates that the run has been canceled. 'Canceling' indicates that the run is in the process of being canceled. 'Paused' indicates that the ongoing run has been paused. 'Failed' indicates that the run has failed. 'Missed' indicates that the run was unable to take place at the scheduled time because the previous run was still happening. 'Succeeded' indicates that the run has finished successfully. 'SucceededWithWarning' indicates that the run finished successfully, but there were some warning messages. 'Skipped' indicates that the run was skipped.")
    __properties: ClassVar[List[str]] = ["awsParams", "azureParams", "id", "name", "cloudspinTaskId", "dataLockConstraints", "endTimeUsecs", "expiryTimeUsecs", "isManuallyDeleted", "message", "onLegalHold", "progressTaskId", "startTimeUsecs", "stats", "status"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped', 'Paused']):
            raise ValueError("must be one of enum values ('Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped', 'Paused')")
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
        """Create an instance of CloudSpinTargetResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of aws_params
        if self.aws_params:
            _dict['awsParams'] = self.aws_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_params
        if self.azure_params:
            _dict['azureParams'] = self.azure_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_lock_constraints
        if self.data_lock_constraints:
            _dict['dataLockConstraints'] = self.data_lock_constraints.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if cloudspin_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.cloudspin_task_id is None and "cloudspin_task_id" in self.model_fields_set:
            _dict['cloudspinTaskId'] = None

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if expiry_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.expiry_time_usecs is None and "expiry_time_usecs" in self.model_fields_set:
            _dict['expiryTimeUsecs'] = None

        # set to None if is_manually_deleted (nullable) is None
        # and model_fields_set contains the field
        if self.is_manually_deleted is None and "is_manually_deleted" in self.model_fields_set:
            _dict['isManuallyDeleted'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if on_legal_hold (nullable) is None
        # and model_fields_set contains the field
        if self.on_legal_hold is None and "on_legal_hold" in self.model_fields_set:
            _dict['onLegalHold'] = None

        # set to None if progress_task_id (nullable) is None
        # and model_fields_set contains the field
        if self.progress_task_id is None and "progress_task_id" in self.model_fields_set:
            _dict['progressTaskId'] = None

        # set to None if start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.start_time_usecs is None and "start_time_usecs" in self.model_fields_set:
            _dict['startTimeUsecs'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CloudSpinTargetResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "awsParams": AwsCloudSpinParams.from_dict(obj["awsParams"]) if obj.get("awsParams") is not None else None,
            "azureParams": AzureCloudSpinParams.from_dict(obj["azureParams"]) if obj.get("azureParams") is not None else None,
            "id": obj.get("id"),
            "name": obj.get("name"),
            "cloudspinTaskId": obj.get("cloudspinTaskId"),
            "dataLockConstraints": DataLockConstraints.from_dict(obj["dataLockConstraints"]) if obj.get("dataLockConstraints") is not None else None,
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "expiryTimeUsecs": obj.get("expiryTimeUsecs"),
            "isManuallyDeleted": obj.get("isManuallyDeleted"),
            "message": obj.get("message"),
            "onLegalHold": obj.get("onLegalHold"),
            "progressTaskId": obj.get("progressTaskId"),
            "startTimeUsecs": obj.get("startTimeUsecs"),
            "stats": CloudSpinDataStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "status": obj.get("status")
        })
        return _obj


