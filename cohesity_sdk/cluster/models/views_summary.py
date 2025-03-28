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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class ViewsSummary(BaseModel):
    """
    Get the summary of the Views.
    """ # noqa: E501
    data_written_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the data written to all the views in bytes.", alias="dataWrittenBytes")
    data_written_bytes_prev: Optional[StrictInt] = Field(default=None, description="Specifies the data written to all the views in bytes at a specific time.", alias="dataWrittenBytesPrev")
    data_written_bytes_prev_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in micro seconds when 'dataWrittenBytesPrev' was calculated.", alias="dataWrittenBytesPrevTimestampUsec")
    data_written_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in micro seconds when 'dataWrittenBytes' was calculated.", alias="dataWrittenBytesTimestampUsec")
    local_tier_resiliency_impact_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the size of the data that has been replicated to other nodes as per RF or Erasure Coding policy.", alias="localTierResiliencyImpactBytes")
    local_tier_resiliency_impact_bytes_prev: Optional[StrictInt] = Field(default=None, description="Specifies the size of the data that has been replicated to other nodes as per RF or Erasure Coding policy at a specific time.", alias="localTierResiliencyImpactBytesPrev")
    local_tier_resiliency_impact_bytes_prev_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in micro seconds when 'localTierResiliencyImpactBytesPrev' was calculated.", alias="localTierResiliencyImpactBytesPrevTimestampUsec")
    local_tier_resiliency_impact_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in micro seconds when 'localTierResiliencyImpactBytes' was calculated.", alias="localTierResiliencyImpactBytesTimestampUsec")
    logical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the logical usage of all the views in bytes.", alias="logicalUsageBytes")
    logical_usage_bytes_prev: Optional[StrictInt] = Field(default=None, description="Specifies the logical usage of all the views in bytes at a specific time.", alias="logicalUsageBytesPrev")
    logical_usage_bytes_prev_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in micro seconds when 'logicalUsageBytesPrev' was calculated.", alias="logicalUsageBytesPrevTimestampUsec")
    logical_usage_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in micro seconds when 'logicalUsageBytes' was calculated.", alias="logicalUsageBytesTimestampUsec")
    num_directories: Optional[StrictInt] = Field(default=None, description="Specifies the number of directories.", alias="numDirectories")
    num_directories_prev: Optional[StrictInt] = Field(default=None, description="Specifies the number of directories at a specific time.", alias="numDirectoriesPrev")
    num_files: Optional[StrictInt] = Field(default=None, description="Specifies the number of files.", alias="numFiles")
    num_files_prev: Optional[StrictInt] = Field(default=None, description="Specifies the number of files at a specific time.", alias="numFilesPrev")
    protected_views: Optional[StrictInt] = Field(default=None, description="Specifies the number of all protected views.", alias="protectedViews")
    replicated_in_views: Optional[StrictInt] = Field(default=None, description="Specifies the number of all the views that are replicated from remote clusters.", alias="replicatedInViews")
    replicated_out_views: Optional[StrictInt] = Field(default=None, description="Specifies the number of all the views that are replicated out to remote clusters.", alias="replicatedOutViews")
    storage_consumed_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the storage consumed of all the views in bytes.", alias="storageConsumedBytes")
    storage_consumed_bytes_prev: Optional[StrictInt] = Field(default=None, description="Specifies the storage consumed by all the views in bytes at a specific time.", alias="storageConsumedBytesPrev")
    storage_consumed_bytes_prev_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in micro seconds when 'storageConsumedBytesPrev' was calculated.", alias="storageConsumedBytesPrevTimestampUsec")
    storage_consumed_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in micro seconds when 'storageConsumedBytes' was calculated.", alias="storageConsumedBytesTimestampUsec")
    total_views: Optional[StrictInt] = Field(default=None, description="Specifies the number of all the views.", alias="totalViews")
    view_entity_id: Optional[StrictStr] = Field(default=None, description="Specifies the entity id of all the views.", alias="viewEntityId")
    __properties: ClassVar[List[str]] = ["dataWrittenBytes", "dataWrittenBytesPrev", "dataWrittenBytesPrevTimestampUsec", "dataWrittenBytesTimestampUsec", "localTierResiliencyImpactBytes", "localTierResiliencyImpactBytesPrev", "localTierResiliencyImpactBytesPrevTimestampUsec", "localTierResiliencyImpactBytesTimestampUsec", "logicalUsageBytes", "logicalUsageBytesPrev", "logicalUsageBytesPrevTimestampUsec", "logicalUsageBytesTimestampUsec", "numDirectories", "numDirectoriesPrev", "numFiles", "numFilesPrev", "protectedViews", "replicatedInViews", "replicatedOutViews", "storageConsumedBytes", "storageConsumedBytesPrev", "storageConsumedBytesPrevTimestampUsec", "storageConsumedBytesTimestampUsec", "totalViews", "viewEntityId"]

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
        """Create an instance of ViewsSummary from a JSON string"""
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
        # set to None if data_written_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.data_written_bytes is None and "data_written_bytes" in self.model_fields_set:
            _dict['dataWrittenBytes'] = None

        # set to None if data_written_bytes_prev (nullable) is None
        # and model_fields_set contains the field
        if self.data_written_bytes_prev is None and "data_written_bytes_prev" in self.model_fields_set:
            _dict['dataWrittenBytesPrev'] = None

        # set to None if data_written_bytes_prev_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.data_written_bytes_prev_timestamp_usec is None and "data_written_bytes_prev_timestamp_usec" in self.model_fields_set:
            _dict['dataWrittenBytesPrevTimestampUsec'] = None

        # set to None if data_written_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.data_written_bytes_timestamp_usec is None and "data_written_bytes_timestamp_usec" in self.model_fields_set:
            _dict['dataWrittenBytesTimestampUsec'] = None

        # set to None if local_tier_resiliency_impact_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.local_tier_resiliency_impact_bytes is None and "local_tier_resiliency_impact_bytes" in self.model_fields_set:
            _dict['localTierResiliencyImpactBytes'] = None

        # set to None if local_tier_resiliency_impact_bytes_prev (nullable) is None
        # and model_fields_set contains the field
        if self.local_tier_resiliency_impact_bytes_prev is None and "local_tier_resiliency_impact_bytes_prev" in self.model_fields_set:
            _dict['localTierResiliencyImpactBytesPrev'] = None

        # set to None if local_tier_resiliency_impact_bytes_prev_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.local_tier_resiliency_impact_bytes_prev_timestamp_usec is None and "local_tier_resiliency_impact_bytes_prev_timestamp_usec" in self.model_fields_set:
            _dict['localTierResiliencyImpactBytesPrevTimestampUsec'] = None

        # set to None if local_tier_resiliency_impact_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.local_tier_resiliency_impact_bytes_timestamp_usec is None and "local_tier_resiliency_impact_bytes_timestamp_usec" in self.model_fields_set:
            _dict['localTierResiliencyImpactBytesTimestampUsec'] = None

        # set to None if logical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.logical_usage_bytes is None and "logical_usage_bytes" in self.model_fields_set:
            _dict['logicalUsageBytes'] = None

        # set to None if logical_usage_bytes_prev (nullable) is None
        # and model_fields_set contains the field
        if self.logical_usage_bytes_prev is None and "logical_usage_bytes_prev" in self.model_fields_set:
            _dict['logicalUsageBytesPrev'] = None

        # set to None if logical_usage_bytes_prev_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.logical_usage_bytes_prev_timestamp_usec is None and "logical_usage_bytes_prev_timestamp_usec" in self.model_fields_set:
            _dict['logicalUsageBytesPrevTimestampUsec'] = None

        # set to None if logical_usage_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.logical_usage_bytes_timestamp_usec is None and "logical_usage_bytes_timestamp_usec" in self.model_fields_set:
            _dict['logicalUsageBytesTimestampUsec'] = None

        # set to None if num_directories (nullable) is None
        # and model_fields_set contains the field
        if self.num_directories is None and "num_directories" in self.model_fields_set:
            _dict['numDirectories'] = None

        # set to None if num_directories_prev (nullable) is None
        # and model_fields_set contains the field
        if self.num_directories_prev is None and "num_directories_prev" in self.model_fields_set:
            _dict['numDirectoriesPrev'] = None

        # set to None if num_files (nullable) is None
        # and model_fields_set contains the field
        if self.num_files is None and "num_files" in self.model_fields_set:
            _dict['numFiles'] = None

        # set to None if num_files_prev (nullable) is None
        # and model_fields_set contains the field
        if self.num_files_prev is None and "num_files_prev" in self.model_fields_set:
            _dict['numFilesPrev'] = None

        # set to None if protected_views (nullable) is None
        # and model_fields_set contains the field
        if self.protected_views is None and "protected_views" in self.model_fields_set:
            _dict['protectedViews'] = None

        # set to None if replicated_in_views (nullable) is None
        # and model_fields_set contains the field
        if self.replicated_in_views is None and "replicated_in_views" in self.model_fields_set:
            _dict['replicatedInViews'] = None

        # set to None if replicated_out_views (nullable) is None
        # and model_fields_set contains the field
        if self.replicated_out_views is None and "replicated_out_views" in self.model_fields_set:
            _dict['replicatedOutViews'] = None

        # set to None if storage_consumed_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.storage_consumed_bytes is None and "storage_consumed_bytes" in self.model_fields_set:
            _dict['storageConsumedBytes'] = None

        # set to None if storage_consumed_bytes_prev (nullable) is None
        # and model_fields_set contains the field
        if self.storage_consumed_bytes_prev is None and "storage_consumed_bytes_prev" in self.model_fields_set:
            _dict['storageConsumedBytesPrev'] = None

        # set to None if storage_consumed_bytes_prev_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.storage_consumed_bytes_prev_timestamp_usec is None and "storage_consumed_bytes_prev_timestamp_usec" in self.model_fields_set:
            _dict['storageConsumedBytesPrevTimestampUsec'] = None

        # set to None if storage_consumed_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.storage_consumed_bytes_timestamp_usec is None and "storage_consumed_bytes_timestamp_usec" in self.model_fields_set:
            _dict['storageConsumedBytesTimestampUsec'] = None

        # set to None if total_views (nullable) is None
        # and model_fields_set contains the field
        if self.total_views is None and "total_views" in self.model_fields_set:
            _dict['totalViews'] = None

        # set to None if view_entity_id (nullable) is None
        # and model_fields_set contains the field
        if self.view_entity_id is None and "view_entity_id" in self.model_fields_set:
            _dict['viewEntityId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViewsSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataWrittenBytes": obj.get("dataWrittenBytes"),
            "dataWrittenBytesPrev": obj.get("dataWrittenBytesPrev"),
            "dataWrittenBytesPrevTimestampUsec": obj.get("dataWrittenBytesPrevTimestampUsec"),
            "dataWrittenBytesTimestampUsec": obj.get("dataWrittenBytesTimestampUsec"),
            "localTierResiliencyImpactBytes": obj.get("localTierResiliencyImpactBytes"),
            "localTierResiliencyImpactBytesPrev": obj.get("localTierResiliencyImpactBytesPrev"),
            "localTierResiliencyImpactBytesPrevTimestampUsec": obj.get("localTierResiliencyImpactBytesPrevTimestampUsec"),
            "localTierResiliencyImpactBytesTimestampUsec": obj.get("localTierResiliencyImpactBytesTimestampUsec"),
            "logicalUsageBytes": obj.get("logicalUsageBytes"),
            "logicalUsageBytesPrev": obj.get("logicalUsageBytesPrev"),
            "logicalUsageBytesPrevTimestampUsec": obj.get("logicalUsageBytesPrevTimestampUsec"),
            "logicalUsageBytesTimestampUsec": obj.get("logicalUsageBytesTimestampUsec"),
            "numDirectories": obj.get("numDirectories"),
            "numDirectoriesPrev": obj.get("numDirectoriesPrev"),
            "numFiles": obj.get("numFiles"),
            "numFilesPrev": obj.get("numFilesPrev"),
            "protectedViews": obj.get("protectedViews"),
            "replicatedInViews": obj.get("replicatedInViews"),
            "replicatedOutViews": obj.get("replicatedOutViews"),
            "storageConsumedBytes": obj.get("storageConsumedBytes"),
            "storageConsumedBytesPrev": obj.get("storageConsumedBytesPrev"),
            "storageConsumedBytesPrevTimestampUsec": obj.get("storageConsumedBytesPrevTimestampUsec"),
            "storageConsumedBytesTimestampUsec": obj.get("storageConsumedBytesTimestampUsec"),
            "totalViews": obj.get("totalViews"),
            "viewEntityId": obj.get("viewEntityId")
        })
        return _obj


