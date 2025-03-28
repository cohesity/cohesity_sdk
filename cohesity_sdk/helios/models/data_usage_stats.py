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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class DataUsageStats(BaseModel):
    """
    Specifies the data usage metric of the data stored on the Cohesity Cluster or Storage Domains (View Boxes).
    """ # noqa: E501
    cloud_data_written_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the total data written on cloud tiers, as computed by the Cohesity Cluster.", alias="cloudDataWrittenBytes")
    cloud_data_written_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of CloudDataWrittenBytes.", alias="cloudDataWrittenBytesTimestampUsec")
    cloud_total_physical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the total cloud capacity, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, compression and deduplication.", alias="cloudTotalPhysicalUsageBytes")
    cloud_total_physical_usage_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of CloudTotalPhysicalUsageBytes.", alias="cloudTotalPhysicalUsageBytesTimestampUsec")
    data_in_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the data read from the protected objects by the Cohesity Cluster before any data reduction using deduplication and compression.", alias="dataInBytes")
    data_in_bytes_after_dedup: Optional[StrictInt] = Field(default=None, description="Specifies the size of the data has been reduced by change-block tracking and deduplication but before compression or data is replicated to other nodes as per RF or Erasure Coding policy.", alias="dataInBytesAfterDedup")
    data_in_bytes_after_dedup_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of DataInBytesAfterDedup.", alias="dataInBytesAfterDedupTimestampUsec")
    data_in_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of DataInBytes.", alias="dataInBytesTimestampUsec")
    data_protect_logical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the logical data used by Data Protect on Cohesity cluster.", alias="dataProtectLogicalUsageBytes")
    data_protect_logical_usage_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of DataProtectLogicalUsageBytes.", alias="dataProtectLogicalUsageBytesTimestampUsec")
    data_protect_physical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the physical data used by Data Protect on Cohesity cluster.", alias="dataProtectPhysicalUsageBytes")
    data_protect_physical_usage_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of DataProtectPhysicalUsageBytes.", alias="dataProtectPhysicalUsageBytesTimestampUsec")
    data_written_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the data written after it has been reduced by deduplication and compression. This does not include resiliency impact.", alias="dataWrittenBytes")
    data_written_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of DataWrittenBytes.", alias="dataWrittenBytesTimestampUsec")
    file_services_logical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the logical data used by File services on Cohesity cluster.", alias="fileServicesLogicalUsageBytes")
    file_services_logical_usage_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of FileServicesLogicalUsageBytes.", alias="fileServicesLogicalUsageBytesTimestampUsec")
    file_services_physical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the physical data used by File services on Cohesity cluster.", alias="fileServicesPhysicalUsageBytes")
    file_services_physical_usage_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of FileServicesPhysicalUsageBytes.", alias="fileServicesPhysicalUsageBytesTimestampUsec")
    local_data_written_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the total data written on local tiers, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, deduplication and compression. This does not include resiliency impact.", alias="localDataWrittenBytes")
    local_data_written_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of LocalDataWrittenBytes.", alias="localDataWrittenBytesTimestampUsec")
    local_tier_resiliency_impact_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the size of the data has been replicated to other nodes as per RF or Erasure Coding policy.", alias="localTierResiliencyImpactBytes")
    local_tier_resiliency_impact_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of LocalTierResiliencyImpactBytes.", alias="localTierResiliencyImpactBytesTimestampUsec")
    local_total_physical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the total local capacity, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, compression and deduplication.", alias="localTotalPhysicalUsageBytes")
    local_total_physical_usage_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of LocalTotalPhysicalUsageBytes.", alias="localTotalPhysicalUsageBytesTimestampUsec")
    num_directories: Optional[StrictInt] = Field(default=None, description="Specifies the number of directories.", alias="numDirectories")
    num_files: Optional[StrictInt] = Field(default=None, description="Specifies the number of files.", alias="numFiles")
    outdated_logical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the logical usage as computed by the Cohesity Cluster. This field is computed on a same frequency as 'StorageConsumedBytes', and it may not be the latest value. It is used to compute reduction ratio.", alias="outdatedLogicalUsageBytes")
    outdated_logical_usage_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of OutdatedLogicalUsageBytes.", alias="outdatedLogicalUsageBytesTimestampUsec")
    storage_consumed_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the total capacity, as computed by the Cohesity Cluster, after the size of the data has been reduced by change-block tracking, compression and deduplication. This includes resiliency impact.", alias="storageConsumedBytes")
    storage_consumed_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of StorageConsumedBytes.", alias="storageConsumedBytesTimestampUsec")
    total_logical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Provides the combined data residing on protected objects. The size of data before reduction by deduplication and compression.", alias="totalLogicalUsageBytes")
    total_logical_usage_bytes_timestamp_usec: Optional[StrictInt] = Field(default=None, description="Specifies Timestamp of TotalLogicalUsageBytes.", alias="totalLogicalUsageBytesTimestampUsec")
    unique_physical_data_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the unique physical data usage in bytes.", alias="uniquePhysicalDataBytes")
    __properties: ClassVar[List[str]] = ["cloudDataWrittenBytes", "cloudDataWrittenBytesTimestampUsec", "cloudTotalPhysicalUsageBytes", "cloudTotalPhysicalUsageBytesTimestampUsec", "dataInBytes", "dataInBytesAfterDedup", "dataInBytesAfterDedupTimestampUsec", "dataInBytesTimestampUsec", "dataProtectLogicalUsageBytes", "dataProtectLogicalUsageBytesTimestampUsec", "dataProtectPhysicalUsageBytes", "dataProtectPhysicalUsageBytesTimestampUsec", "dataWrittenBytes", "dataWrittenBytesTimestampUsec", "fileServicesLogicalUsageBytes", "fileServicesLogicalUsageBytesTimestampUsec", "fileServicesPhysicalUsageBytes", "fileServicesPhysicalUsageBytesTimestampUsec", "localDataWrittenBytes", "localDataWrittenBytesTimestampUsec", "localTierResiliencyImpactBytes", "localTierResiliencyImpactBytesTimestampUsec", "localTotalPhysicalUsageBytes", "localTotalPhysicalUsageBytesTimestampUsec", "numDirectories", "numFiles", "outdatedLogicalUsageBytes", "outdatedLogicalUsageBytesTimestampUsec", "storageConsumedBytes", "storageConsumedBytesTimestampUsec", "totalLogicalUsageBytes", "totalLogicalUsageBytesTimestampUsec", "uniquePhysicalDataBytes"]

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
        """Create an instance of DataUsageStats from a JSON string"""
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
        # set to None if cloud_data_written_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_data_written_bytes is None and "cloud_data_written_bytes" in self.model_fields_set:
            _dict['cloudDataWrittenBytes'] = None

        # set to None if cloud_data_written_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_data_written_bytes_timestamp_usec is None and "cloud_data_written_bytes_timestamp_usec" in self.model_fields_set:
            _dict['cloudDataWrittenBytesTimestampUsec'] = None

        # set to None if cloud_total_physical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_total_physical_usage_bytes is None and "cloud_total_physical_usage_bytes" in self.model_fields_set:
            _dict['cloudTotalPhysicalUsageBytes'] = None

        # set to None if cloud_total_physical_usage_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_total_physical_usage_bytes_timestamp_usec is None and "cloud_total_physical_usage_bytes_timestamp_usec" in self.model_fields_set:
            _dict['cloudTotalPhysicalUsageBytesTimestampUsec'] = None

        # set to None if data_in_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.data_in_bytes is None and "data_in_bytes" in self.model_fields_set:
            _dict['dataInBytes'] = None

        # set to None if data_in_bytes_after_dedup (nullable) is None
        # and model_fields_set contains the field
        if self.data_in_bytes_after_dedup is None and "data_in_bytes_after_dedup" in self.model_fields_set:
            _dict['dataInBytesAfterDedup'] = None

        # set to None if data_in_bytes_after_dedup_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.data_in_bytes_after_dedup_timestamp_usec is None and "data_in_bytes_after_dedup_timestamp_usec" in self.model_fields_set:
            _dict['dataInBytesAfterDedupTimestampUsec'] = None

        # set to None if data_in_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.data_in_bytes_timestamp_usec is None and "data_in_bytes_timestamp_usec" in self.model_fields_set:
            _dict['dataInBytesTimestampUsec'] = None

        # set to None if data_protect_logical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.data_protect_logical_usage_bytes is None and "data_protect_logical_usage_bytes" in self.model_fields_set:
            _dict['dataProtectLogicalUsageBytes'] = None

        # set to None if data_protect_logical_usage_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.data_protect_logical_usage_bytes_timestamp_usec is None and "data_protect_logical_usage_bytes_timestamp_usec" in self.model_fields_set:
            _dict['dataProtectLogicalUsageBytesTimestampUsec'] = None

        # set to None if data_protect_physical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.data_protect_physical_usage_bytes is None and "data_protect_physical_usage_bytes" in self.model_fields_set:
            _dict['dataProtectPhysicalUsageBytes'] = None

        # set to None if data_protect_physical_usage_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.data_protect_physical_usage_bytes_timestamp_usec is None and "data_protect_physical_usage_bytes_timestamp_usec" in self.model_fields_set:
            _dict['dataProtectPhysicalUsageBytesTimestampUsec'] = None

        # set to None if data_written_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.data_written_bytes is None and "data_written_bytes" in self.model_fields_set:
            _dict['dataWrittenBytes'] = None

        # set to None if data_written_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.data_written_bytes_timestamp_usec is None and "data_written_bytes_timestamp_usec" in self.model_fields_set:
            _dict['dataWrittenBytesTimestampUsec'] = None

        # set to None if file_services_logical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.file_services_logical_usage_bytes is None and "file_services_logical_usage_bytes" in self.model_fields_set:
            _dict['fileServicesLogicalUsageBytes'] = None

        # set to None if file_services_logical_usage_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.file_services_logical_usage_bytes_timestamp_usec is None and "file_services_logical_usage_bytes_timestamp_usec" in self.model_fields_set:
            _dict['fileServicesLogicalUsageBytesTimestampUsec'] = None

        # set to None if file_services_physical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.file_services_physical_usage_bytes is None and "file_services_physical_usage_bytes" in self.model_fields_set:
            _dict['fileServicesPhysicalUsageBytes'] = None

        # set to None if file_services_physical_usage_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.file_services_physical_usage_bytes_timestamp_usec is None and "file_services_physical_usage_bytes_timestamp_usec" in self.model_fields_set:
            _dict['fileServicesPhysicalUsageBytesTimestampUsec'] = None

        # set to None if local_data_written_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.local_data_written_bytes is None and "local_data_written_bytes" in self.model_fields_set:
            _dict['localDataWrittenBytes'] = None

        # set to None if local_data_written_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.local_data_written_bytes_timestamp_usec is None and "local_data_written_bytes_timestamp_usec" in self.model_fields_set:
            _dict['localDataWrittenBytesTimestampUsec'] = None

        # set to None if local_tier_resiliency_impact_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.local_tier_resiliency_impact_bytes is None and "local_tier_resiliency_impact_bytes" in self.model_fields_set:
            _dict['localTierResiliencyImpactBytes'] = None

        # set to None if local_tier_resiliency_impact_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.local_tier_resiliency_impact_bytes_timestamp_usec is None and "local_tier_resiliency_impact_bytes_timestamp_usec" in self.model_fields_set:
            _dict['localTierResiliencyImpactBytesTimestampUsec'] = None

        # set to None if local_total_physical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.local_total_physical_usage_bytes is None and "local_total_physical_usage_bytes" in self.model_fields_set:
            _dict['localTotalPhysicalUsageBytes'] = None

        # set to None if local_total_physical_usage_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.local_total_physical_usage_bytes_timestamp_usec is None and "local_total_physical_usage_bytes_timestamp_usec" in self.model_fields_set:
            _dict['localTotalPhysicalUsageBytesTimestampUsec'] = None

        # set to None if num_directories (nullable) is None
        # and model_fields_set contains the field
        if self.num_directories is None and "num_directories" in self.model_fields_set:
            _dict['numDirectories'] = None

        # set to None if num_files (nullable) is None
        # and model_fields_set contains the field
        if self.num_files is None and "num_files" in self.model_fields_set:
            _dict['numFiles'] = None

        # set to None if outdated_logical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.outdated_logical_usage_bytes is None and "outdated_logical_usage_bytes" in self.model_fields_set:
            _dict['outdatedLogicalUsageBytes'] = None

        # set to None if outdated_logical_usage_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.outdated_logical_usage_bytes_timestamp_usec is None and "outdated_logical_usage_bytes_timestamp_usec" in self.model_fields_set:
            _dict['outdatedLogicalUsageBytesTimestampUsec'] = None

        # set to None if storage_consumed_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.storage_consumed_bytes is None and "storage_consumed_bytes" in self.model_fields_set:
            _dict['storageConsumedBytes'] = None

        # set to None if storage_consumed_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.storage_consumed_bytes_timestamp_usec is None and "storage_consumed_bytes_timestamp_usec" in self.model_fields_set:
            _dict['storageConsumedBytesTimestampUsec'] = None

        # set to None if total_logical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.total_logical_usage_bytes is None and "total_logical_usage_bytes" in self.model_fields_set:
            _dict['totalLogicalUsageBytes'] = None

        # set to None if total_logical_usage_bytes_timestamp_usec (nullable) is None
        # and model_fields_set contains the field
        if self.total_logical_usage_bytes_timestamp_usec is None and "total_logical_usage_bytes_timestamp_usec" in self.model_fields_set:
            _dict['totalLogicalUsageBytesTimestampUsec'] = None

        # set to None if unique_physical_data_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.unique_physical_data_bytes is None and "unique_physical_data_bytes" in self.model_fields_set:
            _dict['uniquePhysicalDataBytes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataUsageStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloudDataWrittenBytes": obj.get("cloudDataWrittenBytes"),
            "cloudDataWrittenBytesTimestampUsec": obj.get("cloudDataWrittenBytesTimestampUsec"),
            "cloudTotalPhysicalUsageBytes": obj.get("cloudTotalPhysicalUsageBytes"),
            "cloudTotalPhysicalUsageBytesTimestampUsec": obj.get("cloudTotalPhysicalUsageBytesTimestampUsec"),
            "dataInBytes": obj.get("dataInBytes"),
            "dataInBytesAfterDedup": obj.get("dataInBytesAfterDedup"),
            "dataInBytesAfterDedupTimestampUsec": obj.get("dataInBytesAfterDedupTimestampUsec"),
            "dataInBytesTimestampUsec": obj.get("dataInBytesTimestampUsec"),
            "dataProtectLogicalUsageBytes": obj.get("dataProtectLogicalUsageBytes"),
            "dataProtectLogicalUsageBytesTimestampUsec": obj.get("dataProtectLogicalUsageBytesTimestampUsec"),
            "dataProtectPhysicalUsageBytes": obj.get("dataProtectPhysicalUsageBytes"),
            "dataProtectPhysicalUsageBytesTimestampUsec": obj.get("dataProtectPhysicalUsageBytesTimestampUsec"),
            "dataWrittenBytes": obj.get("dataWrittenBytes"),
            "dataWrittenBytesTimestampUsec": obj.get("dataWrittenBytesTimestampUsec"),
            "fileServicesLogicalUsageBytes": obj.get("fileServicesLogicalUsageBytes"),
            "fileServicesLogicalUsageBytesTimestampUsec": obj.get("fileServicesLogicalUsageBytesTimestampUsec"),
            "fileServicesPhysicalUsageBytes": obj.get("fileServicesPhysicalUsageBytes"),
            "fileServicesPhysicalUsageBytesTimestampUsec": obj.get("fileServicesPhysicalUsageBytesTimestampUsec"),
            "localDataWrittenBytes": obj.get("localDataWrittenBytes"),
            "localDataWrittenBytesTimestampUsec": obj.get("localDataWrittenBytesTimestampUsec"),
            "localTierResiliencyImpactBytes": obj.get("localTierResiliencyImpactBytes"),
            "localTierResiliencyImpactBytesTimestampUsec": obj.get("localTierResiliencyImpactBytesTimestampUsec"),
            "localTotalPhysicalUsageBytes": obj.get("localTotalPhysicalUsageBytes"),
            "localTotalPhysicalUsageBytesTimestampUsec": obj.get("localTotalPhysicalUsageBytesTimestampUsec"),
            "numDirectories": obj.get("numDirectories"),
            "numFiles": obj.get("numFiles"),
            "outdatedLogicalUsageBytes": obj.get("outdatedLogicalUsageBytes"),
            "outdatedLogicalUsageBytesTimestampUsec": obj.get("outdatedLogicalUsageBytesTimestampUsec"),
            "storageConsumedBytes": obj.get("storageConsumedBytes"),
            "storageConsumedBytesTimestampUsec": obj.get("storageConsumedBytesTimestampUsec"),
            "totalLogicalUsageBytes": obj.get("totalLogicalUsageBytes"),
            "totalLogicalUsageBytesTimestampUsec": obj.get("totalLogicalUsageBytesTimestampUsec"),
            "uniquePhysicalDataBytes": obj.get("uniquePhysicalDataBytes")
        })
        return _obj


