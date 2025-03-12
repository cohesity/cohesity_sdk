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
from cohesity_sdk.helios.models.common_nas_object_params import CommonNasObjectParams
from cohesity_sdk.helios.models.flashblade_object_params import FlashbladeObjectParams
from cohesity_sdk.helios.models.group_object_entity_params import GroupObjectEntityParams
from cohesity_sdk.helios.models.isilon_object_params import IsilonObjectParams
from cohesity_sdk.helios.models.mongo_db_object_params import MongoDBObjectParams
from cohesity_sdk.helios.models.mssql_object_entity_params import MssqlObjectEntityParams
from cohesity_sdk.helios.models.netapp_object_params import NetappObjectParams
from cohesity_sdk.helios.models.object_protection_stats_summary import ObjectProtectionStatsSummary
from cohesity_sdk.helios.models.object_snapshots_info import ObjectSnapshotsInfo
from cohesity_sdk.helios.models.object_string_identifier import ObjectStringIdentifier
from cohesity_sdk.helios.models.object_summary import ObjectSummary
from cohesity_sdk.helios.models.object_type_v_center_params import ObjectTypeVCenterParams
from cohesity_sdk.helios.models.object_type_windows_cluster_params import ObjectTypeWindowsClusterParams
from cohesity_sdk.helios.models.oracle_object_entity_params import OracleObjectEntityParams
from cohesity_sdk.helios.models.permission_info import PermissionInfo
from cohesity_sdk.helios.models.physical_object_entity_params import PhysicalObjectEntityParams
from cohesity_sdk.helios.models.sharepoint_object_entity_params import SharepointObjectEntityParams
from cohesity_sdk.helios.models.sharepoint_object_params import SharepointObjectParams
from cohesity_sdk.helios.models.uda_object_params import UdaObjectParams
from cohesity_sdk.helios.models.view_object_params import ViewObjectParams
from cohesity_sdk.helios.models.vmware_object_entity_params import VmwareObjectEntityParams
from typing import Set
from typing_extensions import Self

class ProtectedObject(BaseModel):
    """
    Specifies the Protected Object with last Run's snapshot information per Protection Group.
    """ # noqa: E501
    entity_id: Optional[ObjectStringIdentifier] = Field(default=None, alias="entityId")
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the environment of the object.")
    id: Optional[StrictInt] = Field(default=None, description="Specifies object id.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the object.")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies registered source id to which object belongs.", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies registered source name to which object belongs.", alias="sourceName")
    child_objects: Optional[List[ObjectSummary]] = Field(default=None, description="Specifies child object details.", alias="childObjects")
    global_id: Optional[StrictStr] = Field(default=None, description="Specifies the global id which is a unique identifier of the object.", alias="globalId")
    logical_size_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the logical size of object in bytes.", alias="logicalSizeBytes")
    object_hash: Optional[StrictStr] = Field(default=None, description="Specifies the hash identifier of the object.", alias="objectHash")
    object_type: Optional[StrictStr] = Field(default=None, description="Specifies the type of the object.", alias="objectType")
    os_type: Optional[StrictStr] = Field(default=None, description="Specifies the operating system type of the object.", alias="osType")
    protection_type: Optional[StrictStr] = Field(default=None, description="Specifies the protection type of the object if any.", alias="protectionType")
    sharepoint_site_summary: Optional[SharepointObjectParams] = Field(default=None, alias="sharepointSiteSummary")
    uuid: Optional[StrictStr] = Field(default=None, description="Specifies the uuid which is a unique identifier of the object.")
    v_center_summary: Optional[ObjectTypeVCenterParams] = Field(default=None, alias="vCenterSummary")
    windows_cluster_summary: Optional[ObjectTypeWindowsClusterParams] = Field(default=None, alias="windowsClusterSummary")
    permissions: Optional[PermissionInfo] = None
    protection_stats: Optional[List[ObjectProtectionStatsSummary]] = Field(default=None, description="Specifies the count and size of protected and unprotected objects for the size.", alias="protectionStats")
    elastifile_params: Optional[CommonNasObjectParams] = Field(default=None, alias="elastifileParams")
    flashblade_params: Optional[FlashbladeObjectParams] = Field(default=None, alias="flashbladeParams")
    generic_nas_params: Optional[CommonNasObjectParams] = Field(default=None, alias="genericNasParams")
    gpfs_params: Optional[CommonNasObjectParams] = Field(default=None, alias="gpfsParams")
    group_params: Optional[GroupObjectEntityParams] = Field(default=None, alias="groupParams")
    isilon_params: Optional[IsilonObjectParams] = Field(default=None, alias="isilonParams")
    mongo_db_params: Optional[MongoDBObjectParams] = Field(default=None, alias="mongoDBParams")
    mssql_params: Optional[MssqlObjectEntityParams] = Field(default=None, alias="mssqlParams")
    netapp_params: Optional[NetappObjectParams] = Field(default=None, alias="netappParams")
    oracle_params: Optional[OracleObjectEntityParams] = Field(default=None, alias="oracleParams")
    physical_params: Optional[PhysicalObjectEntityParams] = Field(default=None, alias="physicalParams")
    sharepoint_params: Optional[SharepointObjectEntityParams] = Field(default=None, alias="sharepointParams")
    uda_params: Optional[UdaObjectParams] = Field(default=None, alias="udaParams")
    view_params: Optional[ViewObjectParams] = Field(default=None, alias="viewParams")
    vmware_params: Optional[VmwareObjectEntityParams] = Field(default=None, alias="vmwareParams")
    latest_snapshots_info: Optional[List[ObjectSnapshotsInfo]] = Field(default=None, description="Specifies the latest snapshot information for every Protection Group for a given object.", alias="latestSnapshotsInfo")
    source_info: Optional[ObjectSummary] = Field(default=None, alias="sourceInfo")
    __properties: ClassVar[List[str]] = ["entityId", "environment", "id", "name", "sourceId", "sourceName", "childObjects", "globalId", "logicalSizeBytes", "objectHash", "objectType", "osType", "protectionType", "sharepointSiteSummary", "uuid", "vCenterSummary", "windowsClusterSummary", "permissions", "protectionStats", "elastifileParams", "flashbladeParams", "genericNasParams", "gpfsParams", "groupParams", "isilonParams", "mongoDBParams", "mssqlParams", "netappParams", "oracleParams", "physicalParams", "sharepointParams", "udaParams", "viewParams", "vmwareParams", "latestSnapshotsInfo", "sourceInfo"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc')")
        return value

    @field_validator('object_type')
    def object_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kCluster', 'kVserver', 'kVolume', 'kVCenter', 'kStandaloneHost', 'kvCloudDirector', 'kFolder', 'kDatacenter', 'kComputeResource', 'kClusterComputeResource', 'kResourcePool', 'kDatastore', 'kHostSystem', 'kVirtualMachine', 'kVirtualApp', 'kStoragePod', 'kNetwork', 'kDistributedVirtualPortgroup', 'kTagCategory', 'kTag', 'kOpaqueNetwork', 'kOrganization', 'kVirtualDatacenter', 'kCatalog', 'kOrgMetadata', 'kStoragePolicy', 'kVirtualAppTemplate', 'kDomain', 'kOutlook', 'kMailbox', 'kUsers', 'kGroups', 'kSites', 'kUser', 'kGroup', 'kSite', 'kApplication', 'kGraphUser', 'kPublicFolders', 'kPublicFolder', 'kTeams', 'kTeam', 'kRootPublicFolder', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKeyspace', 'kTable', 'kDatabase', 'kCollection', 'kBucket', 'kNamespace', 'kSCVMMServer', 'kStandaloneCluster', 'kHostGroup', 'kHypervHost', 'kHostCluster', 'kCustomProperty', 'kTenant', 'kSubscription', 'kResourceGroup', 'kStorageAccount', 'kStorageKey', 'kStorageContainer', 'kStorageBlob', 'kApplicationSecurityGroup', 'kNetworkSecurityGroup', 'kVirtualNetwork', 'kSubnet', 'kComputeOptions', 'kSnapshotManagerPermit', 'kAvailabilitySet', 'kSQLServer', 'kSQLDatabase', 'kOVirtManager', 'kHost', 'kStorageDomain', 'kVNicProfile', 'kIAMUser', 'kRegion', 'kAvailabilityZone', 'kEC2Instance', 'kVPC', 'kInstanceType', 'kKeyPair', 'kRDSOptionGroup', 'kRDSParameterGroup', 'kRDSInstance', 'kRDSSubnet', 'kRDSTag', 'kAuroraTag', 'kAuroraCluster', 'kAccount', 'kSubTaskPermit', 'kS3Bucket', 'kS3Tag', 'kKmsKey', 'kRDSPostgresDb', 'kAuroraClusterPostgresDb', 'kProject', 'kLabel', 'kMetadata', 'kVPCConnector', 'kPrismCentral', 'kOtherHypervisorCluster', 'kZone', 'kMountPoint', 'kStorageArray', 'kFileSystem', 'kContainer', 'kFilesystem', 'kFileset', 'kPureProtectionGroup', 'kVolumeGroup', 'kStoragePool', 'kViewBox', 'kView', 'kWindowsCluster', 'kOracleRACCluster', 'kOracleAPCluster', 'kService', 'kPVC', 'kPersistentVolumeClaim', 'kPersistentVolume', 'kRootContainer', 'kDAGRootContainer', 'kExchangeNode', 'kExchangeDAGDatabaseCopy', 'kExchangeStandaloneDatabase', 'kExchangeDAG', 'kExchangeDAGDatabase', 'kDomainController', 'kInstance', 'kAAG', 'kAAGRootContainer', 'kAAGDatabase', 'kRACRootContainer', 'kTableSpace', 'kPDB', 'kObject', 'kOrg', 'kAppInstance']):
            raise ValueError("must be one of enum values ('kCluster', 'kVserver', 'kVolume', 'kVCenter', 'kStandaloneHost', 'kvCloudDirector', 'kFolder', 'kDatacenter', 'kComputeResource', 'kClusterComputeResource', 'kResourcePool', 'kDatastore', 'kHostSystem', 'kVirtualMachine', 'kVirtualApp', 'kStoragePod', 'kNetwork', 'kDistributedVirtualPortgroup', 'kTagCategory', 'kTag', 'kOpaqueNetwork', 'kOrganization', 'kVirtualDatacenter', 'kCatalog', 'kOrgMetadata', 'kStoragePolicy', 'kVirtualAppTemplate', 'kDomain', 'kOutlook', 'kMailbox', 'kUsers', 'kGroups', 'kSites', 'kUser', 'kGroup', 'kSite', 'kApplication', 'kGraphUser', 'kPublicFolders', 'kPublicFolder', 'kTeams', 'kTeam', 'kRootPublicFolder', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKeyspace', 'kTable', 'kDatabase', 'kCollection', 'kBucket', 'kNamespace', 'kSCVMMServer', 'kStandaloneCluster', 'kHostGroup', 'kHypervHost', 'kHostCluster', 'kCustomProperty', 'kTenant', 'kSubscription', 'kResourceGroup', 'kStorageAccount', 'kStorageKey', 'kStorageContainer', 'kStorageBlob', 'kApplicationSecurityGroup', 'kNetworkSecurityGroup', 'kVirtualNetwork', 'kSubnet', 'kComputeOptions', 'kSnapshotManagerPermit', 'kAvailabilitySet', 'kSQLServer', 'kSQLDatabase', 'kOVirtManager', 'kHost', 'kStorageDomain', 'kVNicProfile', 'kIAMUser', 'kRegion', 'kAvailabilityZone', 'kEC2Instance', 'kVPC', 'kInstanceType', 'kKeyPair', 'kRDSOptionGroup', 'kRDSParameterGroup', 'kRDSInstance', 'kRDSSubnet', 'kRDSTag', 'kAuroraTag', 'kAuroraCluster', 'kAccount', 'kSubTaskPermit', 'kS3Bucket', 'kS3Tag', 'kKmsKey', 'kRDSPostgresDb', 'kAuroraClusterPostgresDb', 'kProject', 'kLabel', 'kMetadata', 'kVPCConnector', 'kPrismCentral', 'kOtherHypervisorCluster', 'kZone', 'kMountPoint', 'kStorageArray', 'kFileSystem', 'kContainer', 'kFilesystem', 'kFileset', 'kPureProtectionGroup', 'kVolumeGroup', 'kStoragePool', 'kViewBox', 'kView', 'kWindowsCluster', 'kOracleRACCluster', 'kOracleAPCluster', 'kService', 'kPVC', 'kPersistentVolumeClaim', 'kPersistentVolume', 'kRootContainer', 'kDAGRootContainer', 'kExchangeNode', 'kExchangeDAGDatabaseCopy', 'kExchangeStandaloneDatabase', 'kExchangeDAG', 'kExchangeDAGDatabase', 'kDomainController', 'kInstance', 'kAAG', 'kAAGRootContainer', 'kAAGDatabase', 'kRACRootContainer', 'kTableSpace', 'kPDB', 'kObject', 'kOrg', 'kAppInstance')")
        return value

    @field_validator('os_type')
    def os_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kLinux', 'kWindows', 'kAix', 'kSolaris', 'kSapHana', 'kOther', 'kHPUX', 'kVOS']):
            raise ValueError("must be one of enum values ('kLinux', 'kWindows', 'kAix', 'kSolaris', 'kSapHana', 'kOther', 'kHPUX', 'kVOS')")
        return value

    @field_validator('protection_type')
    def protection_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kAgent', 'kNative', 'kSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsS3', 'kAwsRDSPostgresBackup', 'kAzureSQL', 'kFile', 'kVolume']):
            raise ValueError("must be one of enum values ('kAgent', 'kNative', 'kSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsS3', 'kAwsRDSPostgresBackup', 'kAzureSQL', 'kFile', 'kVolume')")
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
        """Create an instance of ProtectedObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in child_objects (list)
        _items = []
        if self.child_objects:
            for _item_child_objects in self.child_objects:
                if _item_child_objects:
                    _items.append(_item_child_objects.to_dict())
            _dict['childObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of sharepoint_site_summary
        if self.sharepoint_site_summary:
            _dict['sharepointSiteSummary'] = self.sharepoint_site_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of v_center_summary
        if self.v_center_summary:
            _dict['vCenterSummary'] = self.v_center_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of windows_cluster_summary
        if self.windows_cluster_summary:
            _dict['windowsClusterSummary'] = self.windows_cluster_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict['permissions'] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in protection_stats (list)
        _items = []
        if self.protection_stats:
            for _item_protection_stats in self.protection_stats:
                if _item_protection_stats:
                    _items.append(_item_protection_stats.to_dict())
            _dict['protectionStats'] = _items
        # override the default output from pydantic by calling `to_dict()` of elastifile_params
        if self.elastifile_params:
            _dict['elastifileParams'] = self.elastifile_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flashblade_params
        if self.flashblade_params:
            _dict['flashbladeParams'] = self.flashblade_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generic_nas_params
        if self.generic_nas_params:
            _dict['genericNasParams'] = self.generic_nas_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gpfs_params
        if self.gpfs_params:
            _dict['gpfsParams'] = self.gpfs_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of group_params
        if self.group_params:
            _dict['groupParams'] = self.group_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of isilon_params
        if self.isilon_params:
            _dict['isilonParams'] = self.isilon_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mongo_db_params
        if self.mongo_db_params:
            _dict['mongoDBParams'] = self.mongo_db_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mssql_params
        if self.mssql_params:
            _dict['mssqlParams'] = self.mssql_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of netapp_params
        if self.netapp_params:
            _dict['netappParams'] = self.netapp_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oracle_params
        if self.oracle_params:
            _dict['oracleParams'] = self.oracle_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of physical_params
        if self.physical_params:
            _dict['physicalParams'] = self.physical_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sharepoint_params
        if self.sharepoint_params:
            _dict['sharepointParams'] = self.sharepoint_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uda_params
        if self.uda_params:
            _dict['udaParams'] = self.uda_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of view_params
        if self.view_params:
            _dict['viewParams'] = self.view_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vmware_params
        if self.vmware_params:
            _dict['vmwareParams'] = self.vmware_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in latest_snapshots_info (list)
        _items = []
        if self.latest_snapshots_info:
            for _item_latest_snapshots_info in self.latest_snapshots_info:
                if _item_latest_snapshots_info:
                    _items.append(_item_latest_snapshots_info.to_dict())
            _dict['latestSnapshotsInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of source_info
        if self.source_info:
            _dict['sourceInfo'] = self.source_info.to_dict()
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

        # set to None if child_objects (nullable) is None
        # and model_fields_set contains the field
        if self.child_objects is None and "child_objects" in self.model_fields_set:
            _dict['childObjects'] = None

        # set to None if global_id (nullable) is None
        # and model_fields_set contains the field
        if self.global_id is None and "global_id" in self.model_fields_set:
            _dict['globalId'] = None

        # set to None if logical_size_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.logical_size_bytes is None and "logical_size_bytes" in self.model_fields_set:
            _dict['logicalSizeBytes'] = None

        # set to None if object_hash (nullable) is None
        # and model_fields_set contains the field
        if self.object_hash is None and "object_hash" in self.model_fields_set:
            _dict['objectHash'] = None

        # set to None if object_type (nullable) is None
        # and model_fields_set contains the field
        if self.object_type is None and "object_type" in self.model_fields_set:
            _dict['objectType'] = None

        # set to None if os_type (nullable) is None
        # and model_fields_set contains the field
        if self.os_type is None and "os_type" in self.model_fields_set:
            _dict['osType'] = None

        # set to None if protection_type (nullable) is None
        # and model_fields_set contains the field
        if self.protection_type is None and "protection_type" in self.model_fields_set:
            _dict['protectionType'] = None

        # set to None if uuid (nullable) is None
        # and model_fields_set contains the field
        if self.uuid is None and "uuid" in self.model_fields_set:
            _dict['uuid'] = None

        # set to None if protection_stats (nullable) is None
        # and model_fields_set contains the field
        if self.protection_stats is None and "protection_stats" in self.model_fields_set:
            _dict['protectionStats'] = None

        # set to None if view_params (nullable) is None
        # and model_fields_set contains the field
        if self.view_params is None and "view_params" in self.model_fields_set:
            _dict['viewParams'] = None

        # set to None if latest_snapshots_info (nullable) is None
        # and model_fields_set contains the field
        if self.latest_snapshots_info is None and "latest_snapshots_info" in self.model_fields_set:
            _dict['latestSnapshotsInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProtectedObject from a dict"""
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
            "childObjects": [ObjectSummary.from_dict(_item) for _item in obj["childObjects"]] if obj.get("childObjects") is not None else None,
            "globalId": obj.get("globalId"),
            "logicalSizeBytes": obj.get("logicalSizeBytes"),
            "objectHash": obj.get("objectHash"),
            "objectType": obj.get("objectType"),
            "osType": obj.get("osType"),
            "protectionType": obj.get("protectionType"),
            "sharepointSiteSummary": SharepointObjectParams.from_dict(obj["sharepointSiteSummary"]) if obj.get("sharepointSiteSummary") is not None else None,
            "uuid": obj.get("uuid"),
            "vCenterSummary": ObjectTypeVCenterParams.from_dict(obj["vCenterSummary"]) if obj.get("vCenterSummary") is not None else None,
            "windowsClusterSummary": ObjectTypeWindowsClusterParams.from_dict(obj["windowsClusterSummary"]) if obj.get("windowsClusterSummary") is not None else None,
            "permissions": PermissionInfo.from_dict(obj["permissions"]) if obj.get("permissions") is not None else None,
            "protectionStats": [ObjectProtectionStatsSummary.from_dict(_item) for _item in obj["protectionStats"]] if obj.get("protectionStats") is not None else None,
            "elastifileParams": CommonNasObjectParams.from_dict(obj["elastifileParams"]) if obj.get("elastifileParams") is not None else None,
            "flashbladeParams": FlashbladeObjectParams.from_dict(obj["flashbladeParams"]) if obj.get("flashbladeParams") is not None else None,
            "genericNasParams": CommonNasObjectParams.from_dict(obj["genericNasParams"]) if obj.get("genericNasParams") is not None else None,
            "gpfsParams": CommonNasObjectParams.from_dict(obj["gpfsParams"]) if obj.get("gpfsParams") is not None else None,
            "groupParams": GroupObjectEntityParams.from_dict(obj["groupParams"]) if obj.get("groupParams") is not None else None,
            "isilonParams": IsilonObjectParams.from_dict(obj["isilonParams"]) if obj.get("isilonParams") is not None else None,
            "mongoDBParams": MongoDBObjectParams.from_dict(obj["mongoDBParams"]) if obj.get("mongoDBParams") is not None else None,
            "mssqlParams": MssqlObjectEntityParams.from_dict(obj["mssqlParams"]) if obj.get("mssqlParams") is not None else None,
            "netappParams": NetappObjectParams.from_dict(obj["netappParams"]) if obj.get("netappParams") is not None else None,
            "oracleParams": OracleObjectEntityParams.from_dict(obj["oracleParams"]) if obj.get("oracleParams") is not None else None,
            "physicalParams": PhysicalObjectEntityParams.from_dict(obj["physicalParams"]) if obj.get("physicalParams") is not None else None,
            "sharepointParams": SharepointObjectEntityParams.from_dict(obj["sharepointParams"]) if obj.get("sharepointParams") is not None else None,
            "udaParams": UdaObjectParams.from_dict(obj["udaParams"]) if obj.get("udaParams") is not None else None,
            "viewParams": ViewObjectParams.from_dict(obj["viewParams"]) if obj.get("viewParams") is not None else None,
            "vmwareParams": VmwareObjectEntityParams.from_dict(obj["vmwareParams"]) if obj.get("vmwareParams") is not None else None,
            "latestSnapshotsInfo": [ObjectSnapshotsInfo.from_dict(_item) for _item in obj["latestSnapshotsInfo"]] if obj.get("latestSnapshotsInfo") is not None else None,
            "sourceInfo": ObjectSummary.from_dict(obj["sourceInfo"]) if obj.get("sourceInfo") is not None else None
        })
        return _obj


