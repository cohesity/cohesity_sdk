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
from cohesity_sdk.helios.models.archival_target_summary_info import ArchivalTargetSummaryInfo
from typing import Optional, Set
from typing_extensions import Self

class SnapshotsSummary(BaseModel):
    """
    Specifies a summary of the object snapshots.
    """ # noqa: E501
    cluster_id: Optional[StrictInt] = Field(default=None, description="Specifies the cluster id where the snapshots is stored.", alias="clusterId")
    cluster_incarnation_id: Optional[StrictInt] = Field(default=None, description="Specifies the cluster incarnation id where the snapshots is stored.", alias="clusterIncarnationId")
    external_target_info: Optional[ArchivalTargetSummaryInfo] = Field(default=None, alias="externalTargetInfo")
    latest_run_start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in Unix time epoch in microseconds when the latest run started.", alias="latestRunStartTimeUsecs")
    latest_run_status: Optional[StrictStr] = Field(default=None, description="Specifies the status of latest run.", alias="latestRunStatus")
    latest_snapshot_timestamp_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in Unix time epoch in microseconds when the latest snapshot is taken.", alias="latestSnapshotTimestampUsecs")
    ownership_context: Optional[StrictStr] = Field(default=None, description="Specifies the ownership context of the snapshot target.", alias="ownershipContext")
    region_id: Optional[StrictStr] = Field(default=None, description="Specifies the cluster indentifier where the snapshots is stored.", alias="regionId")
    snapshot_count: Optional[StrictInt] = Field(default=None, description="Specifies the number of snapshots of this type and target.", alias="snapshotCount")
    snapshot_target_type: Optional[StrictStr] = Field(default=None, description="Specifies the target type where the Object's snapshot resides.", alias="snapshotTargetType")
    __properties: ClassVar[List[str]] = ["clusterId", "clusterIncarnationId", "externalTargetInfo", "latestRunStartTimeUsecs", "latestRunStatus", "latestSnapshotTimestampUsecs", "ownershipContext", "regionId", "snapshotCount", "snapshotTargetType"]

    @field_validator('latest_run_status')
    def latest_run_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped']):
            raise ValueError("must be one of enum values ('Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped')")
        return value

    @field_validator('ownership_context')
    def ownership_context_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Local', 'FortKnox']):
            raise ValueError("must be one of enum values ('Local', 'FortKnox')")
        return value

    @field_validator('snapshot_target_type')
    def snapshot_target_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Local', 'Archival', 'RpaasArchival', 'StorageArraySnapshot', 'Remote']):
            raise ValueError("must be one of enum values ('Local', 'Archival', 'RpaasArchival', 'StorageArraySnapshot', 'Remote')")
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
        """Create an instance of SnapshotsSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of external_target_info
        if self.external_target_info:
            _dict['externalTargetInfo'] = self.external_target_info.to_dict()
        # set to None if cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_id is None and "cluster_id" in self.model_fields_set:
            _dict['clusterId'] = None

        # set to None if cluster_incarnation_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_incarnation_id is None and "cluster_incarnation_id" in self.model_fields_set:
            _dict['clusterIncarnationId'] = None

        # set to None if latest_run_start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.latest_run_start_time_usecs is None and "latest_run_start_time_usecs" in self.model_fields_set:
            _dict['latestRunStartTimeUsecs'] = None

        # set to None if latest_run_status (nullable) is None
        # and model_fields_set contains the field
        if self.latest_run_status is None and "latest_run_status" in self.model_fields_set:
            _dict['latestRunStatus'] = None

        # set to None if latest_snapshot_timestamp_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.latest_snapshot_timestamp_usecs is None and "latest_snapshot_timestamp_usecs" in self.model_fields_set:
            _dict['latestSnapshotTimestampUsecs'] = None

        # set to None if ownership_context (nullable) is None
        # and model_fields_set contains the field
        if self.ownership_context is None and "ownership_context" in self.model_fields_set:
            _dict['ownershipContext'] = None

        # set to None if region_id (nullable) is None
        # and model_fields_set contains the field
        if self.region_id is None and "region_id" in self.model_fields_set:
            _dict['regionId'] = None

        # set to None if snapshot_count (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_count is None and "snapshot_count" in self.model_fields_set:
            _dict['snapshotCount'] = None

        # set to None if snapshot_target_type (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_target_type is None and "snapshot_target_type" in self.model_fields_set:
            _dict['snapshotTargetType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SnapshotsSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterId": obj.get("clusterId"),
            "clusterIncarnationId": obj.get("clusterIncarnationId"),
            "externalTargetInfo": ArchivalTargetSummaryInfo.from_dict(obj["externalTargetInfo"]) if obj.get("externalTargetInfo") is not None else None,
            "latestRunStartTimeUsecs": obj.get("latestRunStartTimeUsecs"),
            "latestRunStatus": obj.get("latestRunStatus"),
            "latestSnapshotTimestampUsecs": obj.get("latestSnapshotTimestampUsecs"),
            "ownershipContext": obj.get("ownershipContext"),
            "regionId": obj.get("regionId"),
            "snapshotCount": obj.get("snapshotCount"),
            "snapshotTargetType": obj.get("snapshotTargetType")
        })
        return _obj


