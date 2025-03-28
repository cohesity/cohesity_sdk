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
from cohesity_sdk.helios.models.mcm_source_info import McmSourceInfo
from typing import Set
from typing_extensions import Self

class McmSource(BaseModel):
    """
    Specifies a Protection Source on Helios MCM.
    """ # noqa: E501
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the environment of the Protection Source.")
    id: Optional[StrictStr] = Field(default=None, description="Specifies the unique identifier of the Source.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the Protection Source.")
    source_info_list: Optional[List[McmSourceInfo]] = Field(default=None, description="Specifies the Source information list across all platforms.", alias="sourceInfoList")
    type: Optional[StrictStr] = Field(default=None, description="Specifies the object type of the Protection Source.")
    __properties: ClassVar[List[str]] = ["environment", "id", "name", "sourceInfoList", "type"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kAcropolis', 'kKVM', 'kAWS', 'kGCP', 'kAzure', 'kPhysical', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kGPFS', 'kElastifile', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSQL', 'kOracle', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kAcropolis', 'kKVM', 'kAWS', 'kGCP', 'kAzure', 'kPhysical', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kGPFS', 'kElastifile', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSQL', 'kOracle', 'kSfdc')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kCluster', 'kVserver', 'kVolume', 'kVCenter', 'kStandaloneHost', 'kvCloudDirector', 'kFolder', 'kDatacenter', 'kComputeResource', 'kClusterComputeResource', 'kResourcePool', 'kDatastore', 'kHostSystem', 'kVirtualMachine', 'kVirtualApp', 'kStoragePod', 'kNetwork', 'kDistributedVirtualPortgroup', 'kTagCategory', 'kTag', 'kOpaqueNetwork', 'kOrganization', 'kVirtualDatacenter', 'kCatalog', 'kOrgMetadata', 'kStoragePolicy', 'kVirtualAppTemplate', 'kDomain', 'kOutlook', 'kMailbox', 'kUsers', 'kGroups', 'kSites', 'kUser', 'kGroup', 'kSite', 'kApplication', 'kGraphUser', 'kPublicFolders', 'kPublicFolder', 'kTeams', 'kTeam', 'kRootPublicFolder', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKeyspace', 'kTable', 'kDatabase', 'kCollection', 'kBucket', 'kNamespace', 'kSCVMMServer', 'kStandaloneCluster', 'kHostGroup', 'kHypervHost', 'kHostCluster', 'kCustomProperty', 'kTenant', 'kSubscription', 'kResourceGroup', 'kStorageAccount', 'kStorageKey', 'kStorageContainer', 'kStorageBlob', 'kApplicationSecurityGroup', 'kNetworkSecurityGroup', 'kVirtualNetwork', 'kSubnet', 'kComputeOptions', 'kSnapshotManagerPermit', 'kAvailabilitySet', 'kSQLServer', 'kSQLDatabase', 'kOVirtManager', 'kHost', 'kStorageDomain', 'kVNicProfile', 'kIAMUser', 'kRegion', 'kAvailabilityZone', 'kEC2Instance', 'kVPC', 'kInstanceType', 'kKeyPair', 'kRDSOptionGroup', 'kRDSParameterGroup', 'kRDSInstance', 'kRDSSubnet', 'kRDSTag', 'kAuroraTag', 'kAuroraCluster', 'kAccount', 'kSubTaskPermit', 'kS3Bucket', 'kS3Tag', 'kKmsKey', 'kRDSPostgresDb', 'kAuroraClusterPostgresDb', 'kProject', 'kLabel', 'kMetadata', 'kVPCConnector', 'kPrismCentral', 'kOtherHypervisorCluster', 'kZone', 'kMountPoint', 'kStorageArray', 'kFileSystem', 'kContainer', 'kFilesystem', 'kFileset', 'kPureProtectionGroup', 'kVolumeGroup', 'kStoragePool', 'kViewBox', 'kView', 'kWindowsCluster', 'kOracleRACCluster', 'kOracleAPCluster', 'kService', 'kPVC', 'kPersistentVolumeClaim', 'kPersistentVolume', 'kRootContainer', 'kDAGRootContainer', 'kExchangeNode', 'kExchangeDAGDatabaseCopy', 'kExchangeStandaloneDatabase', 'kExchangeDAG', 'kExchangeDAGDatabase', 'kDomainController', 'kInstance', 'kAAG', 'kAAGRootContainer', 'kAAGDatabase', 'kRACRootContainer', 'kTableSpace', 'kPDB', 'kObject', 'kOrg', 'kAppInstance']):
            raise ValueError("must be one of enum values ('kCluster', 'kVserver', 'kVolume', 'kVCenter', 'kStandaloneHost', 'kvCloudDirector', 'kFolder', 'kDatacenter', 'kComputeResource', 'kClusterComputeResource', 'kResourcePool', 'kDatastore', 'kHostSystem', 'kVirtualMachine', 'kVirtualApp', 'kStoragePod', 'kNetwork', 'kDistributedVirtualPortgroup', 'kTagCategory', 'kTag', 'kOpaqueNetwork', 'kOrganization', 'kVirtualDatacenter', 'kCatalog', 'kOrgMetadata', 'kStoragePolicy', 'kVirtualAppTemplate', 'kDomain', 'kOutlook', 'kMailbox', 'kUsers', 'kGroups', 'kSites', 'kUser', 'kGroup', 'kSite', 'kApplication', 'kGraphUser', 'kPublicFolders', 'kPublicFolder', 'kTeams', 'kTeam', 'kRootPublicFolder', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKeyspace', 'kTable', 'kDatabase', 'kCollection', 'kBucket', 'kNamespace', 'kSCVMMServer', 'kStandaloneCluster', 'kHostGroup', 'kHypervHost', 'kHostCluster', 'kCustomProperty', 'kTenant', 'kSubscription', 'kResourceGroup', 'kStorageAccount', 'kStorageKey', 'kStorageContainer', 'kStorageBlob', 'kApplicationSecurityGroup', 'kNetworkSecurityGroup', 'kVirtualNetwork', 'kSubnet', 'kComputeOptions', 'kSnapshotManagerPermit', 'kAvailabilitySet', 'kSQLServer', 'kSQLDatabase', 'kOVirtManager', 'kHost', 'kStorageDomain', 'kVNicProfile', 'kIAMUser', 'kRegion', 'kAvailabilityZone', 'kEC2Instance', 'kVPC', 'kInstanceType', 'kKeyPair', 'kRDSOptionGroup', 'kRDSParameterGroup', 'kRDSInstance', 'kRDSSubnet', 'kRDSTag', 'kAuroraTag', 'kAuroraCluster', 'kAccount', 'kSubTaskPermit', 'kS3Bucket', 'kS3Tag', 'kKmsKey', 'kRDSPostgresDb', 'kAuroraClusterPostgresDb', 'kProject', 'kLabel', 'kMetadata', 'kVPCConnector', 'kPrismCentral', 'kOtherHypervisorCluster', 'kZone', 'kMountPoint', 'kStorageArray', 'kFileSystem', 'kContainer', 'kFilesystem', 'kFileset', 'kPureProtectionGroup', 'kVolumeGroup', 'kStoragePool', 'kViewBox', 'kView', 'kWindowsCluster', 'kOracleRACCluster', 'kOracleAPCluster', 'kService', 'kPVC', 'kPersistentVolumeClaim', 'kPersistentVolume', 'kRootContainer', 'kDAGRootContainer', 'kExchangeNode', 'kExchangeDAGDatabaseCopy', 'kExchangeStandaloneDatabase', 'kExchangeDAG', 'kExchangeDAGDatabase', 'kDomainController', 'kInstance', 'kAAG', 'kAAGRootContainer', 'kAAGDatabase', 'kRACRootContainer', 'kTableSpace', 'kPDB', 'kObject', 'kOrg', 'kAppInstance')")
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
        """Create an instance of McmSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in source_info_list (list)
        _items = []
        if self.source_info_list:
            for _item_source_info_list in self.source_info_list:
                if _item_source_info_list:
                    _items.append(_item_source_info_list.to_dict())
            _dict['sourceInfoList'] = _items
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

        # set to None if source_info_list (nullable) is None
        # and model_fields_set contains the field
        if self.source_info_list is None and "source_info_list" in self.model_fields_set:
            _dict['sourceInfoList'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of McmSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "environment": obj.get("environment"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "sourceInfoList": [McmSourceInfo.from_dict(_item) for _item in obj["sourceInfoList"]] if obj.get("sourceInfoList") is not None else None,
            "type": obj.get("type")
        })
        return _obj


