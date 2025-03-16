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
from typing_extensions import Annotated
from cohesity_sdk.helios.models.archival_target_summary_info import ArchivalTargetSummaryInfo
from cohesity_sdk.helios.models.aws_snapshot_params import AwsSnapshotParams
from cohesity_sdk.helios.models.azure_snapshot_params import AzureSnapshotParams
from cohesity_sdk.helios.models.common_nas_object_params import CommonNasObjectParams
from cohesity_sdk.helios.models.flashblade_object_params import FlashbladeObjectParams
from cohesity_sdk.helios.models.hyperv_snapshot_params import HypervSnapshotParams
from cohesity_sdk.helios.models.isilon_object_params import IsilonObjectParams
from cohesity_sdk.helios.models.netapp_object_params import NetappObjectParams
from cohesity_sdk.helios.models.physical_snapshot_params import PhysicalSnapshotParams
from cohesity_sdk.helios.models.sfdc_object_params import SfdcObjectParams
from typing import Optional, Set
from typing_extensions import Self

class ObjectSnapshot(BaseModel):
    """
    Specifies an Object Snapshot.
    """ # noqa: E501
    aws_params: Optional[AwsSnapshotParams] = Field(default=None, description="Specifies the parameters specific to AWS type snapshot.", alias="awsParams")
    azure_params: Optional[AzureSnapshotParams] = Field(default=None, description="Specifies the parameters specific to Azure type snapshot.", alias="azureParams")
    cluster_id: Optional[StrictInt] = Field(default=None, description="Specifies the cluster id where this snapshot belongs to.", alias="clusterId")
    cluster_incarnation_id: Optional[StrictInt] = Field(default=None, description="Specifies the cluster incarnation id where this snapshot belongs to.", alias="clusterIncarnationId")
    elastifile_params: Optional[CommonNasObjectParams] = Field(default=None, description="Specifies the parameters specific to NetApp type snapshot.", alias="elastifileParams")
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the snapshot environment.")
    expiry_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the expiry time of the snapshot in Unix timestamp epoch in microseconds. If the snapshot has no expiry, this property will not be set.", alias="expiryTimeUsecs")
    external_target_info: Optional[ArchivalTargetSummaryInfo] = Field(default=None, description="Specifies the external target information if this is an archival snapshot.", alias="externalTargetInfo")
    flashblade_params: Optional[FlashbladeObjectParams] = Field(default=None, description="Specifies the parameters specific to Flashblade type snapshot.", alias="flashbladeParams")
    generic_nas_params: Optional[CommonNasObjectParams] = Field(default=None, description="Specifies the parameters specific to Generic NAS type snapshot.", alias="genericNasParams")
    gpfs_params: Optional[CommonNasObjectParams] = Field(default=None, description="Specifies the parameters specific to GPFS type snapshot.", alias="gpfsParams")
    has_data_lock: Optional[StrictBool] = Field(default=None, description="Specifies if this snapshot has datalock.", alias="hasDataLock")
    hyperv_params: Optional[HypervSnapshotParams] = Field(default=None, description="Specifies the parameters specific to HyperV type snapshot.", alias="hypervParams")
    id: Optional[StrictStr] = Field(default=None, description="Specifies the id of the snapshot.")
    indexing_status: Optional[StrictStr] = Field(default=None, description="Specifies the indexing status of objects in this snapshot.<br> 'InProgress' indicates the indexing is in progress.<br> 'Done' indicates indexing is done.<br> 'NoIndex' indicates indexing is not applicable.<br> 'Error' indicates indexing failed with error.", alias="indexingStatus")
    isilon_params: Optional[IsilonObjectParams] = Field(default=None, description="Specifies the parameters specific to Isilon type snapshot.", alias="isilonParams")
    netapp_params: Optional[NetappObjectParams] = Field(default=None, description="Specifies the parameters specific to NetApp type snapshot.", alias="netappParams")
    object_id: Optional[StrictInt] = Field(default=None, description="Specifies the object id which the snapshot is taken from.", alias="objectId")
    object_name: Optional[StrictStr] = Field(default=None, description="Specifies the object name which the snapshot is taken from.", alias="objectName")
    on_legal_hold: Optional[StrictBool] = Field(default=None, description="Specifies if this snapshot is on legalhold.", alias="onLegalHold")
    ownership_context: Optional[StrictStr] = Field(default=None, description="Specifies the ownership context for the target.", alias="ownershipContext")
    physical_params: Optional[PhysicalSnapshotParams] = Field(default=None, description="Specifies the parameters specific to Physical type snapshot.", alias="physicalParams")
    protection_group_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specifies id of the Protection Group.", alias="protectionGroupId")
    protection_group_name: Optional[StrictStr] = Field(default=None, description="Specifies name of the Protection Group.", alias="protectionGroupName")
    protection_group_run_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specifies id of the Protection Group Run.", alias="protectionGroupRunId")
    region_id: Optional[StrictStr] = Field(default=None, description="Specifies the region id where this snapshot belongs to.", alias="regionId")
    run_instance_id: Optional[StrictInt] = Field(default=None, description="Specifies the instance id of the protection run which create the snapshot.", alias="runInstanceId")
    run_start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the start time of the run in micro seconds.", alias="runStartTimeUsecs")
    run_type: Optional[StrictStr] = Field(default=None, description="Specifies the type of protection run created this snapshot.", alias="runType")
    sfdc_params: Optional[SfdcObjectParams] = Field(default=None, description="Specifies the parameters specific to Salesforce type snapshot.", alias="sfdcParams")
    snapshot_target_type: Optional[StrictStr] = Field(default=None, description="Specifies the target type where the Object's snapshot resides.", alias="snapshotTargetType")
    snapshot_timestamp_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in Unix time epoch in microseconds when the snapshot is taken for the specified Object.", alias="snapshotTimestampUsecs")
    source_group_id: Optional[StrictStr] = Field(default=None, description="Specifies the source protection group id in case of replication.", alias="sourceGroupId")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies the object source id which the snapshot is taken from.", alias="sourceId")
    storage_domain_id: Optional[StrictInt] = Field(default=None, description="Specifies the Storage Domain id where the snapshot of object is present.", alias="storageDomainId")
    __properties: ClassVar[List[str]] = ["awsParams", "azureParams", "clusterId", "clusterIncarnationId", "elastifileParams", "environment", "expiryTimeUsecs", "externalTargetInfo", "flashbladeParams", "genericNasParams", "gpfsParams", "hasDataLock", "hypervParams", "id", "indexingStatus", "isilonParams", "netappParams", "objectId", "objectName", "onLegalHold", "ownershipContext", "physicalParams", "protectionGroupId", "protectionGroupName", "protectionGroupRunId", "regionId", "runInstanceId", "runStartTimeUsecs", "runType", "sfdcParams", "snapshotTargetType", "snapshotTimestampUsecs", "sourceGroupId", "sourceId", "storageDomainId"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc')")
        return value

    @field_validator('indexing_status')
    def indexing_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['InProgress', 'Done', 'NoIndex', 'Error']):
            raise ValueError("must be one of enum values ('InProgress', 'Done', 'NoIndex', 'Error')")
        return value

    @field_validator('ownership_context')
    def ownership_context_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Local', 'FortKnox']):
            raise ValueError("must be one of enum values ('Local', 'FortKnox')")
        return value

    @field_validator('protection_group_id')
    def protection_group_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+:\d+:\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+:\d+:\d+$/")
        return value

    @field_validator('protection_group_run_id')
    def protection_group_run_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d+:\d+$", value):
            raise ValueError(r"must validate the regular expression /^\d+:\d+$/")
        return value

    @field_validator('run_type')
    def run_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kRegular', 'kFull', 'kLog', 'kSystem', 'kHydrateCDP', 'kStorageArraySnapshot']):
            raise ValueError("must be one of enum values ('kRegular', 'kFull', 'kLog', 'kSystem', 'kHydrateCDP', 'kStorageArraySnapshot')")
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
        """Create an instance of ObjectSnapshot from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of aws_params
        if self.aws_params:
            _dict['awsParams'] = self.aws_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_params
        if self.azure_params:
            _dict['azureParams'] = self.azure_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of elastifile_params
        if self.elastifile_params:
            _dict['elastifileParams'] = self.elastifile_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_target_info
        if self.external_target_info:
            _dict['externalTargetInfo'] = self.external_target_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flashblade_params
        if self.flashblade_params:
            _dict['flashbladeParams'] = self.flashblade_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generic_nas_params
        if self.generic_nas_params:
            _dict['genericNasParams'] = self.generic_nas_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gpfs_params
        if self.gpfs_params:
            _dict['gpfsParams'] = self.gpfs_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hyperv_params
        if self.hyperv_params:
            _dict['hypervParams'] = self.hyperv_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of isilon_params
        if self.isilon_params:
            _dict['isilonParams'] = self.isilon_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of netapp_params
        if self.netapp_params:
            _dict['netappParams'] = self.netapp_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of physical_params
        if self.physical_params:
            _dict['physicalParams'] = self.physical_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sfdc_params
        if self.sfdc_params:
            _dict['sfdcParams'] = self.sfdc_params.to_dict()
        # set to None if cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_id is None and "cluster_id" in self.model_fields_set:
            _dict['clusterId'] = None

        # set to None if cluster_incarnation_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_incarnation_id is None and "cluster_incarnation_id" in self.model_fields_set:
            _dict['clusterIncarnationId'] = None

        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        # set to None if expiry_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.expiry_time_usecs is None and "expiry_time_usecs" in self.model_fields_set:
            _dict['expiryTimeUsecs'] = None

        # set to None if external_target_info (nullable) is None
        # and model_fields_set contains the field
        if self.external_target_info is None and "external_target_info" in self.model_fields_set:
            _dict['externalTargetInfo'] = None

        # set to None if has_data_lock (nullable) is None
        # and model_fields_set contains the field
        if self.has_data_lock is None and "has_data_lock" in self.model_fields_set:
            _dict['hasDataLock'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if indexing_status (nullable) is None
        # and model_fields_set contains the field
        if self.indexing_status is None and "indexing_status" in self.model_fields_set:
            _dict['indexingStatus'] = None

        # set to None if object_id (nullable) is None
        # and model_fields_set contains the field
        if self.object_id is None and "object_id" in self.model_fields_set:
            _dict['objectId'] = None

        # set to None if object_name (nullable) is None
        # and model_fields_set contains the field
        if self.object_name is None and "object_name" in self.model_fields_set:
            _dict['objectName'] = None

        # set to None if on_legal_hold (nullable) is None
        # and model_fields_set contains the field
        if self.on_legal_hold is None and "on_legal_hold" in self.model_fields_set:
            _dict['onLegalHold'] = None

        # set to None if ownership_context (nullable) is None
        # and model_fields_set contains the field
        if self.ownership_context is None and "ownership_context" in self.model_fields_set:
            _dict['ownershipContext'] = None

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if protection_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_name is None and "protection_group_name" in self.model_fields_set:
            _dict['protectionGroupName'] = None

        # set to None if protection_group_run_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_run_id is None and "protection_group_run_id" in self.model_fields_set:
            _dict['protectionGroupRunId'] = None

        # set to None if region_id (nullable) is None
        # and model_fields_set contains the field
        if self.region_id is None and "region_id" in self.model_fields_set:
            _dict['regionId'] = None

        # set to None if run_instance_id (nullable) is None
        # and model_fields_set contains the field
        if self.run_instance_id is None and "run_instance_id" in self.model_fields_set:
            _dict['runInstanceId'] = None

        # set to None if run_start_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.run_start_time_usecs is None and "run_start_time_usecs" in self.model_fields_set:
            _dict['runStartTimeUsecs'] = None

        # set to None if run_type (nullable) is None
        # and model_fields_set contains the field
        if self.run_type is None and "run_type" in self.model_fields_set:
            _dict['runType'] = None

        # set to None if snapshot_target_type (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_target_type is None and "snapshot_target_type" in self.model_fields_set:
            _dict['snapshotTargetType'] = None

        # set to None if snapshot_timestamp_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.snapshot_timestamp_usecs is None and "snapshot_timestamp_usecs" in self.model_fields_set:
            _dict['snapshotTimestampUsecs'] = None

        # set to None if source_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_group_id is None and "source_group_id" in self.model_fields_set:
            _dict['sourceGroupId'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        # set to None if storage_domain_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_id is None and "storage_domain_id" in self.model_fields_set:
            _dict['storageDomainId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectSnapshot from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "awsParams": AwsSnapshotParams.from_dict(obj["awsParams"]) if obj.get("awsParams") is not None else None,
            "azureParams": AzureSnapshotParams.from_dict(obj["azureParams"]) if obj.get("azureParams") is not None else None,
            "clusterId": obj.get("clusterId"),
            "clusterIncarnationId": obj.get("clusterIncarnationId"),
            "elastifileParams": CommonNasObjectParams.from_dict(obj["elastifileParams"]) if obj.get("elastifileParams") is not None else None,
            "environment": obj.get("environment"),
            "expiryTimeUsecs": obj.get("expiryTimeUsecs"),
            "externalTargetInfo": ArchivalTargetSummaryInfo.from_dict(obj["externalTargetInfo"]) if obj.get("externalTargetInfo") is not None else None,
            "flashbladeParams": FlashbladeObjectParams.from_dict(obj["flashbladeParams"]) if obj.get("flashbladeParams") is not None else None,
            "genericNasParams": CommonNasObjectParams.from_dict(obj["genericNasParams"]) if obj.get("genericNasParams") is not None else None,
            "gpfsParams": CommonNasObjectParams.from_dict(obj["gpfsParams"]) if obj.get("gpfsParams") is not None else None,
            "hasDataLock": obj.get("hasDataLock"),
            "hypervParams": HypervSnapshotParams.from_dict(obj["hypervParams"]) if obj.get("hypervParams") is not None else None,
            "id": obj.get("id"),
            "indexingStatus": obj.get("indexingStatus"),
            "isilonParams": IsilonObjectParams.from_dict(obj["isilonParams"]) if obj.get("isilonParams") is not None else None,
            "netappParams": NetappObjectParams.from_dict(obj["netappParams"]) if obj.get("netappParams") is not None else None,
            "objectId": obj.get("objectId"),
            "objectName": obj.get("objectName"),
            "onLegalHold": obj.get("onLegalHold"),
            "ownershipContext": obj.get("ownershipContext"),
            "physicalParams": PhysicalSnapshotParams.from_dict(obj["physicalParams"]) if obj.get("physicalParams") is not None else None,
            "protectionGroupId": obj.get("protectionGroupId"),
            "protectionGroupName": obj.get("protectionGroupName"),
            "protectionGroupRunId": obj.get("protectionGroupRunId"),
            "regionId": obj.get("regionId"),
            "runInstanceId": obj.get("runInstanceId"),
            "runStartTimeUsecs": obj.get("runStartTimeUsecs"),
            "runType": obj.get("runType"),
            "sfdcParams": SfdcObjectParams.from_dict(obj["sfdcParams"]) if obj.get("sfdcParams") is not None else None,
            "snapshotTargetType": obj.get("snapshotTargetType"),
            "snapshotTimestampUsecs": obj.get("snapshotTimestampUsecs"),
            "sourceGroupId": obj.get("sourceGroupId"),
            "sourceId": obj.get("sourceId"),
            "storageDomainId": obj.get("storageDomainId")
        })
        return _obj


