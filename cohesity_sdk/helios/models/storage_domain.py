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
from cohesity_sdk.helios.models.cloud_down_water_fall_params import CloudDownWaterFallParams
from cohesity_sdk.helios.models.data_usage_stats import DataUsageStats
from cohesity_sdk.helios.models.file_count import FileCount
from cohesity_sdk.helios.models.model_schema import ModelSchema
from cohesity_sdk.helios.models.quota_policy import QuotaPolicy
from cohesity_sdk.helios.models.storage_policy import StoragePolicy
from cohesity_sdk.helios.models.subnet import Subnet
from typing import Set
from typing_extensions import Self

class StorageDomain(BaseModel):
    """
    Specifies a Storage Domain.
    """ # noqa: E501
    ad_domain_name: Optional[StrictStr] = Field(default=None, description="Specifies the Active Directory domain name that this Storage Domain is mapped to.", alias="adDomainName")
    blob_brick_size_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the brick size used for blobs in this Storage Domain.", alias="blobBrickSizeBytes")
    cloud_domain_id: Optional[StrictInt] = Field(default=None, description="Specifies the cloud domain Id.", alias="cloudDomainId")
    cloud_down_water_fall_params: Optional[CloudDownWaterFallParams] = Field(default=None, alias="cloudDownWaterFallParams")
    cluster_partition_id: Optional[StrictInt] = Field(description="Specifies the cluster partition id of the Storage Domain.", alias="clusterPartitionId")
    cluster_partition_name: Optional[StrictStr] = Field(default=None, description="Specifies the cluster partition name of the Storage Domain.", alias="clusterPartitionName")
    default_user_quota: Optional[QuotaPolicy] = Field(default=None, alias="defaultUserQuota")
    default_view_quota: Optional[QuotaPolicy] = Field(default=None, alias="defaultViewQuota")
    dek_rotation_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether DEK(Data Encryption Key) rotation is enabled for this Storage Domain. This is applicable only when the Storage Domain uses AWS or similar KMS in which the KEK (Key Encryption Key) is not created and maintained by Cohesity. For Internal KMS and keys stored in Safenet servers, DEK rotation will not be performed.", alias="dekRotationEnabled")
    direct_archive_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether to enable driect archive on this Storage Domain. If enabled, this Storage Domain can be used as a staging area while copying a large dataset that can't fit on the cluster to an external target.", alias="directArchiveEnabled")
    file_count_by_size: Optional[List[FileCount]] = Field(default=None, description="Specifies the file count by size for the View.", alias="fileCountBySize")
    id: Optional[StrictInt] = Field(default=None, description="Specifies the Storage Domain id.")
    kerberos_realm_name: Optional[StrictStr] = Field(default=None, description="Specifies the Kerberos realm name that this Storage Domain is mapped to.", alias="kerberosRealmName")
    kms_server_id: Optional[StrictInt] = Field(default=None, description="Specifies the associated KMS server id.", alias="kmsServerId")
    last_key_rotation_timestamp_msecs: Optional[StrictInt] = Field(default=None, description="Last key rotation timestamp in msecs for storage domain.", alias="lastKeyRotationTimestampMsecs")
    ldap_provider_id: Optional[StrictInt] = Field(default=None, description="Specifies the LDAP provider id that this Storage Domain is mapped to.", alias="ldapProviderId")
    name: Optional[StrictStr] = Field(description="Specifies the Storage Domain name.")
    nis_domain_names: Optional[List[StrictStr]] = Field(default=None, description="Specifies the NIS domain names that this Storage Domain is mapped to.", alias="nisDomainNames")
    physical_quota: Optional[QuotaPolicy] = Field(default=None, alias="physicalQuota")
    recommended: Optional[StrictBool] = Field(default=None, description="Specifies whether Storage Domain is recommended for the specified View template.")
    removal_state: Optional[StrictStr] = Field(default=None, description="Specifies the current removal state of the Storage Domain. 'DontRemove' means the state of object is functional and it is not being removed. 'MarkedForRemoval' means the object is being removed. 'OkToRemove' means the object has been removed on the Cohesity Cluster and if the object is physical, it can be removed from the Cohesity Cluster.", alias="removalState")
    s3_buckets_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether to enable creation of S3 bucket on this Storage Domain.", alias="s3BucketsEnabled")
    schemas: Optional[List[ModelSchema]] = Field(default=None, description="Specifies the Storage Domain schemas.")
    stats: Optional[DataUsageStats] = None
    storage_policy: Optional[StoragePolicy] = Field(default=None, alias="storagePolicy")
    subnet_whitelist: Optional[List[Subnet]] = Field(default=None, description="Specifies a list of Subnets with IP addresses that have permissions to access the Storage Domain.", alias="subnetWhitelist")
    tenant_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of tenant ids that that Storage Domain belongs. There can only be one tenant id in this field unless Storage Domain sharing between tenants is allowed on this cluster.", alias="tenantIds")
    treat_file_sync_as_data_sync: Optional[StrictBool] = Field(default=None, description="If 'true', when the Cohesity Cluster is writing to a file, the file modification time is not persisted synchronously during the file write, so the modification time may not be accurate. (Typically the file modification time is off by 30 seconds but it can be longer.)", alias="treatFileSyncAsDataSync")
    vault_id: Optional[StrictInt] = Field(default=None, description="Specifies the vault Id associated with cloud domain ID.", alias="vaultId")
    __properties: ClassVar[List[str]] = ["adDomainName", "blobBrickSizeBytes", "cloudDomainId", "cloudDownWaterFallParams", "clusterPartitionId", "clusterPartitionName", "defaultUserQuota", "defaultViewQuota", "dekRotationEnabled", "directArchiveEnabled", "fileCountBySize", "id", "kerberosRealmName", "kmsServerId", "lastKeyRotationTimestampMsecs", "ldapProviderId", "name", "nisDomainNames", "physicalQuota", "recommended", "removalState", "s3BucketsEnabled", "schemas", "stats", "storagePolicy", "subnetWhitelist", "tenantIds", "treatFileSyncAsDataSync", "vaultId"]

    @field_validator('removal_state')
    def removal_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DontRemove', 'MarkedForRemoval', 'OkToRemove']):
            raise ValueError("must be one of enum values ('DontRemove', 'MarkedForRemoval', 'OkToRemove')")
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
        """Create an instance of StorageDomain from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "cluster_partition_name",
            "file_count_by_size",
            "id",
            "recommended",
            "removal_state",
            "schemas",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cloud_down_water_fall_params
        if self.cloud_down_water_fall_params:
            _dict['cloudDownWaterFallParams'] = self.cloud_down_water_fall_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_user_quota
        if self.default_user_quota:
            _dict['defaultUserQuota'] = self.default_user_quota.to_dict()
        # override the default output from pydantic by calling `to_dict()` of default_view_quota
        if self.default_view_quota:
            _dict['defaultViewQuota'] = self.default_view_quota.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in file_count_by_size (list)
        _items = []
        if self.file_count_by_size:
            for _item_file_count_by_size in self.file_count_by_size:
                if _item_file_count_by_size:
                    _items.append(_item_file_count_by_size.to_dict())
            _dict['fileCountBySize'] = _items
        # override the default output from pydantic by calling `to_dict()` of physical_quota
        if self.physical_quota:
            _dict['physicalQuota'] = self.physical_quota.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in schemas (list)
        _items = []
        if self.schemas:
            for _item_schemas in self.schemas:
                if _item_schemas:
                    _items.append(_item_schemas.to_dict())
            _dict['schemas'] = _items
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage_policy
        if self.storage_policy:
            _dict['storagePolicy'] = self.storage_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in subnet_whitelist (list)
        _items = []
        if self.subnet_whitelist:
            for _item_subnet_whitelist in self.subnet_whitelist:
                if _item_subnet_whitelist:
                    _items.append(_item_subnet_whitelist.to_dict())
            _dict['subnetWhitelist'] = _items
        # set to None if ad_domain_name (nullable) is None
        # and model_fields_set contains the field
        if self.ad_domain_name is None and "ad_domain_name" in self.model_fields_set:
            _dict['adDomainName'] = None

        # set to None if blob_brick_size_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.blob_brick_size_bytes is None and "blob_brick_size_bytes" in self.model_fields_set:
            _dict['blobBrickSizeBytes'] = None

        # set to None if cloud_domain_id (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_domain_id is None and "cloud_domain_id" in self.model_fields_set:
            _dict['cloudDomainId'] = None

        # set to None if cluster_partition_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_partition_id is None and "cluster_partition_id" in self.model_fields_set:
            _dict['clusterPartitionId'] = None

        # set to None if cluster_partition_name (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_partition_name is None and "cluster_partition_name" in self.model_fields_set:
            _dict['clusterPartitionName'] = None

        # set to None if dek_rotation_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.dek_rotation_enabled is None and "dek_rotation_enabled" in self.model_fields_set:
            _dict['dekRotationEnabled'] = None

        # set to None if direct_archive_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.direct_archive_enabled is None and "direct_archive_enabled" in self.model_fields_set:
            _dict['directArchiveEnabled'] = None

        # set to None if file_count_by_size (nullable) is None
        # and model_fields_set contains the field
        if self.file_count_by_size is None and "file_count_by_size" in self.model_fields_set:
            _dict['fileCountBySize'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if kerberos_realm_name (nullable) is None
        # and model_fields_set contains the field
        if self.kerberos_realm_name is None and "kerberos_realm_name" in self.model_fields_set:
            _dict['kerberosRealmName'] = None

        # set to None if kms_server_id (nullable) is None
        # and model_fields_set contains the field
        if self.kms_server_id is None and "kms_server_id" in self.model_fields_set:
            _dict['kmsServerId'] = None

        # set to None if last_key_rotation_timestamp_msecs (nullable) is None
        # and model_fields_set contains the field
        if self.last_key_rotation_timestamp_msecs is None and "last_key_rotation_timestamp_msecs" in self.model_fields_set:
            _dict['lastKeyRotationTimestampMsecs'] = None

        # set to None if ldap_provider_id (nullable) is None
        # and model_fields_set contains the field
        if self.ldap_provider_id is None and "ldap_provider_id" in self.model_fields_set:
            _dict['ldapProviderId'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if nis_domain_names (nullable) is None
        # and model_fields_set contains the field
        if self.nis_domain_names is None and "nis_domain_names" in self.model_fields_set:
            _dict['nisDomainNames'] = None

        # set to None if recommended (nullable) is None
        # and model_fields_set contains the field
        if self.recommended is None and "recommended" in self.model_fields_set:
            _dict['recommended'] = None

        # set to None if removal_state (nullable) is None
        # and model_fields_set contains the field
        if self.removal_state is None and "removal_state" in self.model_fields_set:
            _dict['removalState'] = None

        # set to None if s3_buckets_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.s3_buckets_enabled is None and "s3_buckets_enabled" in self.model_fields_set:
            _dict['s3BucketsEnabled'] = None

        # set to None if schemas (nullable) is None
        # and model_fields_set contains the field
        if self.schemas is None and "schemas" in self.model_fields_set:
            _dict['schemas'] = None

        # set to None if subnet_whitelist (nullable) is None
        # and model_fields_set contains the field
        if self.subnet_whitelist is None and "subnet_whitelist" in self.model_fields_set:
            _dict['subnetWhitelist'] = None

        # set to None if tenant_ids (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_ids is None and "tenant_ids" in self.model_fields_set:
            _dict['tenantIds'] = None

        # set to None if treat_file_sync_as_data_sync (nullable) is None
        # and model_fields_set contains the field
        if self.treat_file_sync_as_data_sync is None and "treat_file_sync_as_data_sync" in self.model_fields_set:
            _dict['treatFileSyncAsDataSync'] = None

        # set to None if vault_id (nullable) is None
        # and model_fields_set contains the field
        if self.vault_id is None and "vault_id" in self.model_fields_set:
            _dict['vaultId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StorageDomain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adDomainName": obj.get("adDomainName"),
            "blobBrickSizeBytes": obj.get("blobBrickSizeBytes"),
            "cloudDomainId": obj.get("cloudDomainId"),
            "cloudDownWaterFallParams": CloudDownWaterFallParams.from_dict(obj["cloudDownWaterFallParams"]) if obj.get("cloudDownWaterFallParams") is not None else None,
            "clusterPartitionId": obj.get("clusterPartitionId"),
            "clusterPartitionName": obj.get("clusterPartitionName"),
            "defaultUserQuota": QuotaPolicy.from_dict(obj["defaultUserQuota"]) if obj.get("defaultUserQuota") is not None else None,
            "defaultViewQuota": QuotaPolicy.from_dict(obj["defaultViewQuota"]) if obj.get("defaultViewQuota") is not None else None,
            "dekRotationEnabled": obj.get("dekRotationEnabled"),
            "directArchiveEnabled": obj.get("directArchiveEnabled"),
            "fileCountBySize": [FileCount.from_dict(_item) for _item in obj["fileCountBySize"]] if obj.get("fileCountBySize") is not None else None,
            "id": obj.get("id"),
            "kerberosRealmName": obj.get("kerberosRealmName"),
            "kmsServerId": obj.get("kmsServerId"),
            "lastKeyRotationTimestampMsecs": obj.get("lastKeyRotationTimestampMsecs"),
            "ldapProviderId": obj.get("ldapProviderId"),
            "name": obj.get("name"),
            "nisDomainNames": obj.get("nisDomainNames"),
            "physicalQuota": QuotaPolicy.from_dict(obj["physicalQuota"]) if obj.get("physicalQuota") is not None else None,
            "recommended": obj.get("recommended"),
            "removalState": obj.get("removalState"),
            "s3BucketsEnabled": obj.get("s3BucketsEnabled"),
            "schemas": [ModelSchema.from_dict(_item) for _item in obj["schemas"]] if obj.get("schemas") is not None else None,
            "stats": DataUsageStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "storagePolicy": StoragePolicy.from_dict(obj["storagePolicy"]) if obj.get("storagePolicy") is not None else None,
            "subnetWhitelist": [Subnet.from_dict(_item) for _item in obj["subnetWhitelist"]] if obj.get("subnetWhitelist") is not None else None,
            "tenantIds": obj.get("tenantIds"),
            "treatFileSyncAsDataSync": obj.get("treatFileSyncAsDataSync"),
            "vaultId": obj.get("vaultId")
        })
        return _obj


