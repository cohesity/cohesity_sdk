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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.acl_config import AclConfig
from cohesity_sdk.cluster.models.antivirus_scan_config import AntivirusScanConfig
from cohesity_sdk.cluster.models.bucket_policy import BucketPolicy
from cohesity_sdk.cluster.models.file_extension_filter import FileExtensionFilter
from cohesity_sdk.cluster.models.file_level_data_lock_config import FileLevelDataLockConfig
from cohesity_sdk.cluster.models.filer_lifecycle_management import FilerLifecycleManagement
from cohesity_sdk.cluster.models.nfs_root_permissions import NfsRootPermissions
from cohesity_sdk.cluster.models.nfs_squash import NfsSquash
from cohesity_sdk.cluster.models.nis_netgroups import NisNetgroups
from cohesity_sdk.cluster.models.qo_s import QoS
from cohesity_sdk.cluster.models.quota_policy import QuotaPolicy
from cohesity_sdk.cluster.models.s3_config_owner_info import S3ConfigOwnerInfo
from cohesity_sdk.cluster.models.s3_lifecycle_management import S3LifecycleManagement
from cohesity_sdk.cluster.models.self_service_snapshot_config import SelfServiceSnapshotConfig
from cohesity_sdk.cluster.models.smb_permissions_info import SmbPermissionsInfo
from cohesity_sdk.cluster.models.storage_policy_override import StoragePolicyOverride
from cohesity_sdk.cluster.models.subnet import Subnet
from cohesity_sdk.cluster.models.view_pinning_config import ViewPinningConfig
from cohesity_sdk.cluster.models.view_protocol import ViewProtocol
from cohesity_sdk.cluster.models.view_share_permissions import ViewSharePermissions
from typing import Set
from typing_extensions import Self

class UpdateViewParam(BaseModel):
    """
    Specifies the settings that define a View. Common fields between create, edit and response struct.
    """ # noqa: E501
    enable_nfs_kerberos_authentication: Optional[StrictBool] = Field(default=None, description="If set, it enables NFS Kerberos Authentication", alias="enableNfsKerberosAuthentication")
    enable_nfs_kerberos_integrity: Optional[StrictBool] = Field(default=None, description="If set, it enables NFS Kerberos Integrity", alias="enableNfsKerberosIntegrity")
    enable_nfs_kerberos_privacy: Optional[StrictBool] = Field(default=None, description="If set, it enables NFS Kerberos Privacy", alias="enableNfsKerberosPrivacy")
    enable_nfs_unix_authentication: Optional[StrictBool] = Field(default=None, description="If set, it enables NFS UNIX Authentication", alias="enableNfsUnixAuthentication")
    enable_nfs_view_discovery: Optional[StrictBool] = Field(default=None, description="If set, it enables discovery of view for NFS.", alias="enableNfsViewDiscovery")
    enable_nfs_wcc: Optional[StrictBool] = Field(default=None, description="If set, it enables NFS weak cache consistency.", alias="enableNfsWcc")
    nfs_all_squash: Optional[NfsSquash] = Field(default=None, alias="nfsAllSquash")
    nfs_root_permissions: Optional[NfsRootPermissions] = Field(default=None, alias="nfsRootPermissions")
    nfs_root_squash: Optional[NfsSquash] = Field(default=None, alias="nfsRootSquash")
    enable_fast_durable_handle: Optional[StrictBool] = Field(default=None, description="Specifies whether fast durable handle is enabled. If enabled, view open handle will be kept in memory, which results in a higher performance. But the handles cannot be recovered if node or service crashes.", alias="enableFastDurableHandle")
    enable_smb_access_based_enumeration: Optional[StrictBool] = Field(default=None, description="Specifies if access-based enumeration should be enabled. If 'true', only files and folders that the user has permissions to access are visible on the SMB share for that user.", alias="enableSmbAccessBasedEnumeration")
    enable_smb_encryption: Optional[StrictBool] = Field(default=None, description="Specifies the SMB encryption for the View. If set, it enables the SMB encryption for the View. Encryption is supported only by SMB 3.x dialects. Dialects that do not support would still access data in unencrypted format.", alias="enableSmbEncryption")
    enable_smb_oplock: Optional[StrictBool] = Field(default=None, description="Specifies whether SMB opportunistic lock is enabled.", alias="enableSmbOplock")
    enable_smb_view_discovery: Optional[StrictBool] = Field(default=None, description="If set, it enables discovery of view for SMB.", alias="enableSmbViewDiscovery")
    enforce_smb_encryption: Optional[StrictBool] = Field(default=None, description="Specifies the SMB encryption for all the sessions for the View. If set, encryption is enforced for all the sessions for the View. When enabled all future and existing unencrypted sessions are disallowed.", alias="enforceSmbEncryption")
    share_permissions: Optional[ViewSharePermissions] = Field(default=None, alias="sharePermissions")
    smb_permissions_info: Optional[SmbPermissionsInfo] = Field(default=None, alias="smbPermissionsInfo")
    acl_config: Optional[AclConfig] = Field(default=None, alias="aclConfig")
    bucket_policy: Optional[BucketPolicy] = Field(default=None, alias="bucketPolicy")
    enable_abac: Optional[StrictBool] = Field(default=None, description="Specifies if this View has S3 ABAC enabled. This can only be set while creating a view. The ABAC server corresponding the tenant will be used for authentication and authorization checks. ", alias="enableAbac")
    lifecycle_management: Optional[S3LifecycleManagement] = Field(default=None, alias="lifecycleManagement")
    owner_info: Optional[S3ConfigOwnerInfo] = Field(default=None, alias="ownerInfo")
    s3_access_path: Optional[StrictStr] = Field(default=None, description="Specifies the path to access this View as an S3 share.", alias="s3AccessPath")
    versioning: Optional[StrictStr] = Field(default=None, description="Specifies the versioning state of S3 bucket. Buckets can be in one of three states: UnVersioned (default), VersioningEnabled, or VersioningSuspended. Once versioning is enabled for a bucket, it can never return to an UnVersioned state. However, versioning on the bucket can be suspended.")
    swift_project_domain: Optional[StrictStr] = Field(default=None, description="Specifies the Keystone project domain.", alias="swiftProjectDomain")
    swift_project_name: Optional[StrictStr] = Field(default=None, description="Specifies the Keystone project name.", alias="swiftProjectName")
    swift_user_domain: Optional[StrictStr] = Field(default=None, description="Specifies the Keystone user domain.", alias="swiftUserDomain")
    swift_username: Optional[StrictStr] = Field(default=None, description="Specifies the Keystone username.", alias="swiftUsername")
    access_sids: Optional[List[StrictStr]] = Field(default=None, description="Array of Security Identifiers (SIDs) Specifies the list of security identifiers (SIDs) for the restricted Principals who have access to this View.", alias="accessSids")
    allow_mount_on_windows: Optional[StrictBool] = Field(default=None, description="Specifies if this View can be mounted using the NFS protocol on Windows systems. If true, this View can be NFS mounted on Windows systems.", alias="allowMountOnWindows")
    antivirus_scan_config: Optional[AntivirusScanConfig] = Field(default=None, alias="antivirusScanConfig")
    category: Optional[StrictStr] = Field(default=None, description="Specifies the category of the View.")
    description: Optional[StrictStr] = Field(default=None, description="Specifies an optional text description about the View.")
    enable_filer_audit_logging: Optional[StrictBool] = Field(default=None, description="Specifies if Filer Audit Logging is enabled for this view.", alias="enableFilerAuditLogging")
    enable_live_indexing: Optional[StrictBool] = Field(default=None, description="Specifies whether to enable live indexing for the view.", alias="enableLiveIndexing")
    enable_metadata_accelerator: Optional[StrictBool] = Field(default=None, description="Specifies if metadata accelerator is enabled for this view. Only supported while creating a view.", alias="enableMetadataAccelerator")
    enable_minion: Optional[StrictBool] = Field(default=None, description="Specifies if this view should allow minion or not. If true, this will allow minion.", alias="enableMinion")
    enable_offline_caching: Optional[StrictBool] = Field(default=None, description="Specifies whether to enable offline file caching of the view.", alias="enableOfflineCaching")
    file_extension_filter: Optional[FileExtensionFilter] = Field(default=None, alias="fileExtensionFilter")
    file_lock_config: Optional[FileLevelDataLockConfig] = Field(default=None, alias="fileLockConfig")
    filer_lifecycle_management: Optional[FilerLifecycleManagement] = Field(default=None, alias="filerLifecycleManagement")
    is_externally_triggered_backup_target: Optional[StrictBool] = Field(default=None, description="Specifies whether the view is for externally triggered backup target. If so, Magneto will ignore the backup schedule for the view protection job of this view. By default it is disabled.", alias="isExternallyTriggeredBackupTarget")
    is_read_only: Optional[StrictBool] = Field(default=None, description="Specifies if the view is a read only view. User will no longer be able to write to this view if this is set to true.", alias="isReadOnly")
    lexicographic_prefetch: Optional[StrictBool] = Field(default=None, description="If small files are accessed sequentially from a client, this specifies whether to detect and prefetch files based on the lexicographic index to improve file read performance.", alias="lexicographicPrefetch")
    logical_quota: Optional[QuotaPolicy] = Field(default=None, alias="logicalQuota")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the View.")
    netgroup_whitelist: Optional[NisNetgroups] = Field(default=None, alias="netgroupWhitelist")
    override_global_netgroup_whitelist: Optional[StrictBool] = Field(default=None, description="Specifies whether view level client netgroup whitelist overrides cluster and global setting.", alias="overrideGlobalNetgroupWhitelist")
    override_global_subnet_whitelist: Optional[StrictBool] = Field(default=None, description="Specifies whether view level client subnet whitelist overrides cluster and global setting.", alias="overrideGlobalSubnetWhitelist")
    protocol_access: Optional[List[ViewProtocol]] = Field(default=None, description="Specifies the supported Protocols for the View.", alias="protocolAccess")
    qos: Optional[QoS] = None
    security_mode: Optional[StrictStr] = Field(default=None, description="Specifies the security mode used for this view. Currently we support the following modes: Native, Unified and NTFS style. 'NativeMode' indicates a native security mode. 'UnifiedMode' indicates a unified security mode. 'NtfsMode' indicates a NTFS style security mode.", alias="securityMode")
    self_service_snapshot_config: Optional[SelfServiceSnapshotConfig] = Field(default=None, alias="selfServiceSnapshotConfig")
    storage_policy_override: Optional[StoragePolicyOverride] = Field(default=None, alias="storagePolicyOverride")
    subnet_whitelist: Optional[List[Subnet]] = Field(default=None, description="Array of Subnets. Specifies a list of Subnets with IP addresses that have permissions to access the View. (Overrides or extends the Subnets specified at the global Cohesity Cluster level.)", alias="subnetWhitelist")
    tenant_id: Optional[StrictStr] = Field(default=None, description="Optional tenant id who has access to this View.", alias="tenantId")
    view_lock_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether view lock is enabled. If enabled the view cannot be modified or deleted until unlock. By default it is disabled.", alias="viewLockEnabled")
    view_pinning_config: Optional[ViewPinningConfig] = Field(default=None, alias="viewPinningConfig")
    __properties: ClassVar[List[str]] = ["enableNfsKerberosAuthentication", "enableNfsKerberosIntegrity", "enableNfsKerberosPrivacy", "enableNfsUnixAuthentication", "enableNfsViewDiscovery", "enableNfsWcc", "nfsAllSquash", "nfsRootPermissions", "nfsRootSquash", "enableFastDurableHandle", "enableSmbAccessBasedEnumeration", "enableSmbEncryption", "enableSmbOplock", "enableSmbViewDiscovery", "enforceSmbEncryption", "sharePermissions", "smbPermissionsInfo", "aclConfig", "bucketPolicy", "enableAbac", "lifecycleManagement", "ownerInfo", "s3AccessPath", "versioning", "swiftProjectDomain", "swiftProjectName", "swiftUserDomain", "swiftUsername", "accessSids", "allowMountOnWindows", "antivirusScanConfig", "category", "description", "enableFilerAuditLogging", "enableLiveIndexing", "enableMetadataAccelerator", "enableMinion", "enableOfflineCaching", "fileExtensionFilter", "fileLockConfig", "filerLifecycleManagement", "isExternallyTriggeredBackupTarget", "isReadOnly", "lexicographicPrefetch", "logicalQuota", "name", "netgroupWhitelist", "overrideGlobalNetgroupWhitelist", "overrideGlobalSubnetWhitelist", "protocolAccess", "qos", "securityMode", "selfServiceSnapshotConfig", "storagePolicyOverride", "subnetWhitelist", "tenantId", "viewLockEnabled", "viewPinningConfig"]

    @field_validator('versioning')
    def versioning_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['UnVersioned', 'Enabled', 'Suspended']):
            raise ValueError("must be one of enum values ('UnVersioned', 'Enabled', 'Suspended')")
        return value

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BackupTarget', 'FileServices', 'ObjectServices']):
            raise ValueError("must be one of enum values ('BackupTarget', 'FileServices', 'ObjectServices')")
        return value

    @field_validator('security_mode')
    def security_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NativeMode', 'UnifiedMode', 'NtfsMode']):
            raise ValueError("must be one of enum values ('NativeMode', 'UnifiedMode', 'NtfsMode')")
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
        """Create an instance of UpdateViewParam from a JSON string"""
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
            "s3_access_path",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of nfs_all_squash
        if self.nfs_all_squash:
            _dict['nfsAllSquash'] = self.nfs_all_squash.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nfs_root_permissions
        if self.nfs_root_permissions:
            _dict['nfsRootPermissions'] = self.nfs_root_permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nfs_root_squash
        if self.nfs_root_squash:
            _dict['nfsRootSquash'] = self.nfs_root_squash.to_dict()
        # override the default output from pydantic by calling `to_dict()` of share_permissions
        if self.share_permissions:
            _dict['sharePermissions'] = self.share_permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of smb_permissions_info
        if self.smb_permissions_info:
            _dict['smbPermissionsInfo'] = self.smb_permissions_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of acl_config
        if self.acl_config:
            _dict['aclConfig'] = self.acl_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bucket_policy
        if self.bucket_policy:
            _dict['bucketPolicy'] = self.bucket_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lifecycle_management
        if self.lifecycle_management:
            _dict['lifecycleManagement'] = self.lifecycle_management.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner_info
        if self.owner_info:
            _dict['ownerInfo'] = self.owner_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of antivirus_scan_config
        if self.antivirus_scan_config:
            _dict['antivirusScanConfig'] = self.antivirus_scan_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file_extension_filter
        if self.file_extension_filter:
            _dict['fileExtensionFilter'] = self.file_extension_filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file_lock_config
        if self.file_lock_config:
            _dict['fileLockConfig'] = self.file_lock_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filer_lifecycle_management
        if self.filer_lifecycle_management:
            _dict['filerLifecycleManagement'] = self.filer_lifecycle_management.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logical_quota
        if self.logical_quota:
            _dict['logicalQuota'] = self.logical_quota.to_dict()
        # override the default output from pydantic by calling `to_dict()` of netgroup_whitelist
        if self.netgroup_whitelist:
            _dict['netgroupWhitelist'] = self.netgroup_whitelist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in protocol_access (list)
        _items = []
        if self.protocol_access:
            for _item_protocol_access in self.protocol_access:
                if _item_protocol_access:
                    _items.append(_item_protocol_access.to_dict())
            _dict['protocolAccess'] = _items
        # override the default output from pydantic by calling `to_dict()` of qos
        if self.qos:
            _dict['qos'] = self.qos.to_dict()
        # override the default output from pydantic by calling `to_dict()` of self_service_snapshot_config
        if self.self_service_snapshot_config:
            _dict['selfServiceSnapshotConfig'] = self.self_service_snapshot_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage_policy_override
        if self.storage_policy_override:
            _dict['storagePolicyOverride'] = self.storage_policy_override.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in subnet_whitelist (list)
        _items = []
        if self.subnet_whitelist:
            for _item_subnet_whitelist in self.subnet_whitelist:
                if _item_subnet_whitelist:
                    _items.append(_item_subnet_whitelist.to_dict())
            _dict['subnetWhitelist'] = _items
        # override the default output from pydantic by calling `to_dict()` of view_pinning_config
        if self.view_pinning_config:
            _dict['viewPinningConfig'] = self.view_pinning_config.to_dict()
        # set to None if enable_nfs_kerberos_authentication (nullable) is None
        # and model_fields_set contains the field
        if self.enable_nfs_kerberos_authentication is None and "enable_nfs_kerberos_authentication" in self.model_fields_set:
            _dict['enableNfsKerberosAuthentication'] = None

        # set to None if enable_nfs_kerberos_integrity (nullable) is None
        # and model_fields_set contains the field
        if self.enable_nfs_kerberos_integrity is None and "enable_nfs_kerberos_integrity" in self.model_fields_set:
            _dict['enableNfsKerberosIntegrity'] = None

        # set to None if enable_nfs_kerberos_privacy (nullable) is None
        # and model_fields_set contains the field
        if self.enable_nfs_kerberos_privacy is None and "enable_nfs_kerberos_privacy" in self.model_fields_set:
            _dict['enableNfsKerberosPrivacy'] = None

        # set to None if enable_nfs_unix_authentication (nullable) is None
        # and model_fields_set contains the field
        if self.enable_nfs_unix_authentication is None and "enable_nfs_unix_authentication" in self.model_fields_set:
            _dict['enableNfsUnixAuthentication'] = None

        # set to None if enable_nfs_view_discovery (nullable) is None
        # and model_fields_set contains the field
        if self.enable_nfs_view_discovery is None and "enable_nfs_view_discovery" in self.model_fields_set:
            _dict['enableNfsViewDiscovery'] = None

        # set to None if enable_nfs_wcc (nullable) is None
        # and model_fields_set contains the field
        if self.enable_nfs_wcc is None and "enable_nfs_wcc" in self.model_fields_set:
            _dict['enableNfsWcc'] = None

        # set to None if enable_fast_durable_handle (nullable) is None
        # and model_fields_set contains the field
        if self.enable_fast_durable_handle is None and "enable_fast_durable_handle" in self.model_fields_set:
            _dict['enableFastDurableHandle'] = None

        # set to None if enable_smb_access_based_enumeration (nullable) is None
        # and model_fields_set contains the field
        if self.enable_smb_access_based_enumeration is None and "enable_smb_access_based_enumeration" in self.model_fields_set:
            _dict['enableSmbAccessBasedEnumeration'] = None

        # set to None if enable_smb_encryption (nullable) is None
        # and model_fields_set contains the field
        if self.enable_smb_encryption is None and "enable_smb_encryption" in self.model_fields_set:
            _dict['enableSmbEncryption'] = None

        # set to None if enable_smb_oplock (nullable) is None
        # and model_fields_set contains the field
        if self.enable_smb_oplock is None and "enable_smb_oplock" in self.model_fields_set:
            _dict['enableSmbOplock'] = None

        # set to None if enable_smb_view_discovery (nullable) is None
        # and model_fields_set contains the field
        if self.enable_smb_view_discovery is None and "enable_smb_view_discovery" in self.model_fields_set:
            _dict['enableSmbViewDiscovery'] = None

        # set to None if enforce_smb_encryption (nullable) is None
        # and model_fields_set contains the field
        if self.enforce_smb_encryption is None and "enforce_smb_encryption" in self.model_fields_set:
            _dict['enforceSmbEncryption'] = None

        # set to None if enable_abac (nullable) is None
        # and model_fields_set contains the field
        if self.enable_abac is None and "enable_abac" in self.model_fields_set:
            _dict['enableAbac'] = None

        # set to None if s3_access_path (nullable) is None
        # and model_fields_set contains the field
        if self.s3_access_path is None and "s3_access_path" in self.model_fields_set:
            _dict['s3AccessPath'] = None

        # set to None if versioning (nullable) is None
        # and model_fields_set contains the field
        if self.versioning is None and "versioning" in self.model_fields_set:
            _dict['versioning'] = None

        # set to None if swift_project_domain (nullable) is None
        # and model_fields_set contains the field
        if self.swift_project_domain is None and "swift_project_domain" in self.model_fields_set:
            _dict['swiftProjectDomain'] = None

        # set to None if swift_project_name (nullable) is None
        # and model_fields_set contains the field
        if self.swift_project_name is None and "swift_project_name" in self.model_fields_set:
            _dict['swiftProjectName'] = None

        # set to None if swift_user_domain (nullable) is None
        # and model_fields_set contains the field
        if self.swift_user_domain is None and "swift_user_domain" in self.model_fields_set:
            _dict['swiftUserDomain'] = None

        # set to None if swift_username (nullable) is None
        # and model_fields_set contains the field
        if self.swift_username is None and "swift_username" in self.model_fields_set:
            _dict['swiftUsername'] = None

        # set to None if access_sids (nullable) is None
        # and model_fields_set contains the field
        if self.access_sids is None and "access_sids" in self.model_fields_set:
            _dict['accessSids'] = None

        # set to None if allow_mount_on_windows (nullable) is None
        # and model_fields_set contains the field
        if self.allow_mount_on_windows is None and "allow_mount_on_windows" in self.model_fields_set:
            _dict['allowMountOnWindows'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if enable_filer_audit_logging (nullable) is None
        # and model_fields_set contains the field
        if self.enable_filer_audit_logging is None and "enable_filer_audit_logging" in self.model_fields_set:
            _dict['enableFilerAuditLogging'] = None

        # set to None if enable_live_indexing (nullable) is None
        # and model_fields_set contains the field
        if self.enable_live_indexing is None and "enable_live_indexing" in self.model_fields_set:
            _dict['enableLiveIndexing'] = None

        # set to None if enable_metadata_accelerator (nullable) is None
        # and model_fields_set contains the field
        if self.enable_metadata_accelerator is None and "enable_metadata_accelerator" in self.model_fields_set:
            _dict['enableMetadataAccelerator'] = None

        # set to None if enable_minion (nullable) is None
        # and model_fields_set contains the field
        if self.enable_minion is None and "enable_minion" in self.model_fields_set:
            _dict['enableMinion'] = None

        # set to None if enable_offline_caching (nullable) is None
        # and model_fields_set contains the field
        if self.enable_offline_caching is None and "enable_offline_caching" in self.model_fields_set:
            _dict['enableOfflineCaching'] = None

        # set to None if is_externally_triggered_backup_target (nullable) is None
        # and model_fields_set contains the field
        if self.is_externally_triggered_backup_target is None and "is_externally_triggered_backup_target" in self.model_fields_set:
            _dict['isExternallyTriggeredBackupTarget'] = None

        # set to None if is_read_only (nullable) is None
        # and model_fields_set contains the field
        if self.is_read_only is None and "is_read_only" in self.model_fields_set:
            _dict['isReadOnly'] = None

        # set to None if lexicographic_prefetch (nullable) is None
        # and model_fields_set contains the field
        if self.lexicographic_prefetch is None and "lexicographic_prefetch" in self.model_fields_set:
            _dict['lexicographicPrefetch'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if override_global_netgroup_whitelist (nullable) is None
        # and model_fields_set contains the field
        if self.override_global_netgroup_whitelist is None and "override_global_netgroup_whitelist" in self.model_fields_set:
            _dict['overrideGlobalNetgroupWhitelist'] = None

        # set to None if override_global_subnet_whitelist (nullable) is None
        # and model_fields_set contains the field
        if self.override_global_subnet_whitelist is None and "override_global_subnet_whitelist" in self.model_fields_set:
            _dict['overrideGlobalSubnetWhitelist'] = None

        # set to None if protocol_access (nullable) is None
        # and model_fields_set contains the field
        if self.protocol_access is None and "protocol_access" in self.model_fields_set:
            _dict['protocolAccess'] = None

        # set to None if security_mode (nullable) is None
        # and model_fields_set contains the field
        if self.security_mode is None and "security_mode" in self.model_fields_set:
            _dict['securityMode'] = None

        # set to None if storage_policy_override (nullable) is None
        # and model_fields_set contains the field
        if self.storage_policy_override is None and "storage_policy_override" in self.model_fields_set:
            _dict['storagePolicyOverride'] = None

        # set to None if subnet_whitelist (nullable) is None
        # and model_fields_set contains the field
        if self.subnet_whitelist is None and "subnet_whitelist" in self.model_fields_set:
            _dict['subnetWhitelist'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if view_lock_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.view_lock_enabled is None and "view_lock_enabled" in self.model_fields_set:
            _dict['viewLockEnabled'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateViewParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enableNfsKerberosAuthentication": obj.get("enableNfsKerberosAuthentication"),
            "enableNfsKerberosIntegrity": obj.get("enableNfsKerberosIntegrity"),
            "enableNfsKerberosPrivacy": obj.get("enableNfsKerberosPrivacy"),
            "enableNfsUnixAuthentication": obj.get("enableNfsUnixAuthentication"),
            "enableNfsViewDiscovery": obj.get("enableNfsViewDiscovery"),
            "enableNfsWcc": obj.get("enableNfsWcc"),
            "nfsAllSquash": NfsSquash.from_dict(obj["nfsAllSquash"]) if obj.get("nfsAllSquash") is not None else None,
            "nfsRootPermissions": NfsRootPermissions.from_dict(obj["nfsRootPermissions"]) if obj.get("nfsRootPermissions") is not None else None,
            "nfsRootSquash": NfsSquash.from_dict(obj["nfsRootSquash"]) if obj.get("nfsRootSquash") is not None else None,
            "enableFastDurableHandle": obj.get("enableFastDurableHandle"),
            "enableSmbAccessBasedEnumeration": obj.get("enableSmbAccessBasedEnumeration"),
            "enableSmbEncryption": obj.get("enableSmbEncryption"),
            "enableSmbOplock": obj.get("enableSmbOplock"),
            "enableSmbViewDiscovery": obj.get("enableSmbViewDiscovery"),
            "enforceSmbEncryption": obj.get("enforceSmbEncryption"),
            "sharePermissions": ViewSharePermissions.from_dict(obj["sharePermissions"]) if obj.get("sharePermissions") is not None else None,
            "smbPermissionsInfo": SmbPermissionsInfo.from_dict(obj["smbPermissionsInfo"]) if obj.get("smbPermissionsInfo") is not None else None,
            "aclConfig": AclConfig.from_dict(obj["aclConfig"]) if obj.get("aclConfig") is not None else None,
            "bucketPolicy": BucketPolicy.from_dict(obj["bucketPolicy"]) if obj.get("bucketPolicy") is not None else None,
            "enableAbac": obj.get("enableAbac"),
            "lifecycleManagement": S3LifecycleManagement.from_dict(obj["lifecycleManagement"]) if obj.get("lifecycleManagement") is not None else None,
            "ownerInfo": S3ConfigOwnerInfo.from_dict(obj["ownerInfo"]) if obj.get("ownerInfo") is not None else None,
            "s3AccessPath": obj.get("s3AccessPath"),
            "versioning": obj.get("versioning"),
            "swiftProjectDomain": obj.get("swiftProjectDomain"),
            "swiftProjectName": obj.get("swiftProjectName"),
            "swiftUserDomain": obj.get("swiftUserDomain"),
            "swiftUsername": obj.get("swiftUsername"),
            "accessSids": obj.get("accessSids"),
            "allowMountOnWindows": obj.get("allowMountOnWindows"),
            "antivirusScanConfig": AntivirusScanConfig.from_dict(obj["antivirusScanConfig"]) if obj.get("antivirusScanConfig") is not None else None,
            "category": obj.get("category"),
            "description": obj.get("description"),
            "enableFilerAuditLogging": obj.get("enableFilerAuditLogging"),
            "enableLiveIndexing": obj.get("enableLiveIndexing"),
            "enableMetadataAccelerator": obj.get("enableMetadataAccelerator"),
            "enableMinion": obj.get("enableMinion"),
            "enableOfflineCaching": obj.get("enableOfflineCaching"),
            "fileExtensionFilter": FileExtensionFilter.from_dict(obj["fileExtensionFilter"]) if obj.get("fileExtensionFilter") is not None else None,
            "fileLockConfig": FileLevelDataLockConfig.from_dict(obj["fileLockConfig"]) if obj.get("fileLockConfig") is not None else None,
            "filerLifecycleManagement": FilerLifecycleManagement.from_dict(obj["filerLifecycleManagement"]) if obj.get("filerLifecycleManagement") is not None else None,
            "isExternallyTriggeredBackupTarget": obj.get("isExternallyTriggeredBackupTarget"),
            "isReadOnly": obj.get("isReadOnly"),
            "lexicographicPrefetch": obj.get("lexicographicPrefetch"),
            "logicalQuota": QuotaPolicy.from_dict(obj["logicalQuota"]) if obj.get("logicalQuota") is not None else None,
            "name": obj.get("name"),
            "netgroupWhitelist": NisNetgroups.from_dict(obj["netgroupWhitelist"]) if obj.get("netgroupWhitelist") is not None else None,
            "overrideGlobalNetgroupWhitelist": obj.get("overrideGlobalNetgroupWhitelist"),
            "overrideGlobalSubnetWhitelist": obj.get("overrideGlobalSubnetWhitelist"),
            "protocolAccess": [ViewProtocol.from_dict(_item) for _item in obj["protocolAccess"]] if obj.get("protocolAccess") is not None else None,
            "qos": QoS.from_dict(obj["qos"]) if obj.get("qos") is not None else None,
            "securityMode": obj.get("securityMode"),
            "selfServiceSnapshotConfig": SelfServiceSnapshotConfig.from_dict(obj["selfServiceSnapshotConfig"]) if obj.get("selfServiceSnapshotConfig") is not None else None,
            "storagePolicyOverride": StoragePolicyOverride.from_dict(obj["storagePolicyOverride"]) if obj.get("storagePolicyOverride") is not None else None,
            "subnetWhitelist": [Subnet.from_dict(_item) for _item in obj["subnetWhitelist"]] if obj.get("subnetWhitelist") is not None else None,
            "tenantId": obj.get("tenantId"),
            "viewLockEnabled": obj.get("viewLockEnabled"),
            "viewPinningConfig": ViewPinningConfig.from_dict(obj["viewPinningConfig"]) if obj.get("viewPinningConfig") is not None else None
        })
        return _obj


