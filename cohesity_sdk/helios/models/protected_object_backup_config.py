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
from cohesity_sdk.helios.models.aws_object_protection_response_params import AwsObjectProtectionResponseParams
from cohesity_sdk.helios.models.azure_object_protection_response_params import AzureObjectProtectionResponseParams
from cohesity_sdk.helios.models.common_mssql_object_protection_params import CommonMssqlObjectProtectionParams
from cohesity_sdk.helios.models.elastifile_object_protection_response_params import ElastifileObjectProtectionResponseParams
from cohesity_sdk.helios.models.flashblade_object_protection_response_params import FlashbladeObjectProtectionResponseParams
from cohesity_sdk.helios.models.generic_nas_object_protection_response_params import GenericNasObjectProtectionResponseParams
from cohesity_sdk.helios.models.gpfs_object_protection_response_params import GpfsObjectProtectionResponseParams
from cohesity_sdk.helios.models.hyper_v_object_protection_response_params import HyperVObjectProtectionResponseParams
from cohesity_sdk.helios.models.isilon_object_protection_response_params import IsilonObjectProtectionResponseParams
from cohesity_sdk.helios.models.netapp_object_protection_response_params import NetappObjectProtectionResponseParams
from cohesity_sdk.helios.models.office365_object_protection_params import Office365ObjectProtectionParams
from cohesity_sdk.helios.models.oracle_object_based_protection_params import OracleObjectBasedProtectionParams
from cohesity_sdk.helios.models.physical_object_protection_params import PhysicalObjectProtectionParams
from cohesity_sdk.helios.models.policy_config import PolicyConfig
from cohesity_sdk.helios.models.sfdc_object_protection_params import SfdcObjectProtectionParams
from cohesity_sdk.helios.models.sla_rule import SlaRule
from cohesity_sdk.helios.models.time_of_day import TimeOfDay
from cohesity_sdk.helios.models.uda_object_protection_params import UdaObjectProtectionParams
from cohesity_sdk.helios.models.vmware_object_protection_response_params import VmwareObjectProtectionResponseParams
from typing import Set
from typing_extensions import Self

class ProtectedObjectBackupConfig(BaseModel):
    """
    Specifies the backup configuration for protected object.
    """ # noqa: E501
    abort_in_blackouts: Optional[StrictBool] = Field(default=None, description="Specifies whether currently executing object backup should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false.", alias="abortInBlackouts")
    end_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won't be ended.", alias="endTimeUsecs")
    policy_config: Optional[PolicyConfig] = Field(default=None, alias="policyConfig")
    policy_id: Optional[StrictStr] = Field(default=None, description="Specifies the unique id of the Protection Policy. The Policy settings will be attached with every object and will be used in backup.", alias="policyId")
    priority: Optional[StrictStr] = Field(default=None, description="Specifies the priority for the objects backup.")
    qos_policy: Optional[StrictStr] = Field(default=None, description="Specifies whether object backup will be written to HDD or SSD.", alias="qosPolicy")
    skip_rigel_for_backup: Optional[StrictBool] = Field(default=None, description="Specifies whether to skip Rigel for backup or not.", alias="skipRigelForBackup")
    sla: Optional[List[SlaRule]] = Field(default=None, description="Specifies the SLA parameters for list of objects.")
    start_time: Optional[TimeOfDay] = Field(default=None, alias="startTime")
    storage_domain_id: Optional[StrictInt] = Field(default=None, description="Specifies the Storage Domain (View Box) ID where the object backup will be taken. This is not required if Cloud archive direct is benig used.", alias="storageDomainId")
    aws_params: Optional[AwsObjectProtectionResponseParams] = Field(default=None, alias="awsParams")
    azure_params: Optional[AzureObjectProtectionResponseParams] = Field(default=None, alias="azureParams")
    elastifile_params: Optional[ElastifileObjectProtectionResponseParams] = Field(default=None, alias="elastifileParams")
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the environment for current object.")
    flashblade_params: Optional[FlashbladeObjectProtectionResponseParams] = Field(default=None, alias="flashbladeParams")
    generic_nas_params: Optional[GenericNasObjectProtectionResponseParams] = Field(default=None, alias="genericNasParams")
    gpfs_params: Optional[GpfsObjectProtectionResponseParams] = Field(default=None, alias="gpfsParams")
    hyperv_params: Optional[HyperVObjectProtectionResponseParams] = Field(default=None, alias="hypervParams")
    isilon_params: Optional[IsilonObjectProtectionResponseParams] = Field(default=None, alias="isilonParams")
    mssql_params: Optional[CommonMssqlObjectProtectionParams] = Field(default=None, alias="mssqlParams")
    netapp_params: Optional[NetappObjectProtectionResponseParams] = Field(default=None, alias="netappParams")
    office365_params: Optional[Office365ObjectProtectionParams] = Field(default=None, alias="office365Params")
    oracle_params: Optional[OracleObjectBasedProtectionParams] = Field(default=None, alias="oracleParams")
    physical_params: Optional[PhysicalObjectProtectionParams] = Field(default=None, alias="physicalParams")
    sfdc_params: Optional[SfdcObjectProtectionParams] = Field(default=None, alias="sfdcParams")
    uda_params: Optional[UdaObjectProtectionParams] = Field(default=None, alias="udaParams")
    vmware_params: Optional[VmwareObjectProtectionResponseParams] = Field(default=None, alias="vmwareParams")
    auto_protect_parent_id: Optional[StrictInt] = Field(default=None, description="Specifies the parent ID of the object which the backup configuration is applied to if this is an auto protect config.", alias="autoProtectParentId")
    is_active: Optional[StrictBool] = Field(default=None, description="Specifies whether or not protection has been deactivated on this object.", alias="isActive")
    is_auto_protect_config: Optional[StrictBool] = Field(default=None, description="Specifies whether or not this configuration is applied to an autoprotected object rather than this specific object.", alias="isAutoProtectConfig")
    is_paused: Optional[StrictBool] = Field(default=None, description="Specifies whether or not protection has been paused on this object.", alias="isPaused")
    __properties: ClassVar[List[str]] = ["abortInBlackouts", "endTimeUsecs", "policyConfig", "policyId", "priority", "qosPolicy", "skipRigelForBackup", "sla", "startTime", "storageDomainId", "awsParams", "azureParams", "elastifileParams", "environment", "flashbladeParams", "genericNasParams", "gpfsParams", "hypervParams", "isilonParams", "mssqlParams", "netappParams", "office365Params", "oracleParams", "physicalParams", "sfdcParams", "udaParams", "vmwareParams", "autoProtectParentId", "isActive", "isAutoProtectConfig", "isPaused"]

    @field_validator('priority')
    def priority_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kLow', 'kMedium', 'kHigh']):
            raise ValueError("must be one of enum values ('kLow', 'kMedium', 'kHigh')")
        return value

    @field_validator('qos_policy')
    def qos_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kBackupHDD', 'kBackupSSD', 'kTestAndDevHigh', 'kBackupAll']):
            raise ValueError("must be one of enum values ('kBackupHDD', 'kBackupSSD', 'kTestAndDevHigh', 'kBackupAll')")
        return value

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kVCD', 'kAzure', 'kGCP', 'kKVM', 'kAcropolis', 'kAWS', 'kAWSNative', 'kAwsS3', 'kAWSSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSQL', 'kAzureSnapshotManager', 'kPhysical', 'kPhysicalFiles', 'kGPFS', 'kElastifile', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kPure', 'kIbmFlashSystem', 'kSQL', 'kExchange', 'kAD', 'kOracle', 'kView', 'kRemoteAdapter', 'kO365', 'kO365PublicFolders', 'kO365Teams', 'kO365Group', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kVCD', 'kAzure', 'kGCP', 'kKVM', 'kAcropolis', 'kAWS', 'kAWSNative', 'kAwsS3', 'kAWSSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSQL', 'kAzureSnapshotManager', 'kPhysical', 'kPhysicalFiles', 'kGPFS', 'kElastifile', 'kNetapp', 'kGenericNas', 'kIsilon', 'kFlashBlade', 'kPure', 'kIbmFlashSystem', 'kSQL', 'kExchange', 'kAD', 'kOracle', 'kView', 'kRemoteAdapter', 'kO365', 'kO365PublicFolders', 'kO365Teams', 'kO365Group', 'kO365Exchange', 'kO365OneDrive', 'kO365Sharepoint', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc')")
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
        """Create an instance of ProtectedObjectBackupConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of policy_config
        if self.policy_config:
            _dict['policyConfig'] = self.policy_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sla (list)
        _items = []
        if self.sla:
            for _item_sla in self.sla:
                if _item_sla:
                    _items.append(_item_sla.to_dict())
            _dict['sla'] = _items
        # override the default output from pydantic by calling `to_dict()` of start_time
        if self.start_time:
            _dict['startTime'] = self.start_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_params
        if self.aws_params:
            _dict['awsParams'] = self.aws_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of azure_params
        if self.azure_params:
            _dict['azureParams'] = self.azure_params.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of hyperv_params
        if self.hyperv_params:
            _dict['hypervParams'] = self.hyperv_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of isilon_params
        if self.isilon_params:
            _dict['isilonParams'] = self.isilon_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mssql_params
        if self.mssql_params:
            _dict['mssqlParams'] = self.mssql_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of netapp_params
        if self.netapp_params:
            _dict['netappParams'] = self.netapp_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of office365_params
        if self.office365_params:
            _dict['office365Params'] = self.office365_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of oracle_params
        if self.oracle_params:
            _dict['oracleParams'] = self.oracle_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of physical_params
        if self.physical_params:
            _dict['physicalParams'] = self.physical_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sfdc_params
        if self.sfdc_params:
            _dict['sfdcParams'] = self.sfdc_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uda_params
        if self.uda_params:
            _dict['udaParams'] = self.uda_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vmware_params
        if self.vmware_params:
            _dict['vmwareParams'] = self.vmware_params.to_dict()
        # set to None if abort_in_blackouts (nullable) is None
        # and model_fields_set contains the field
        if self.abort_in_blackouts is None and "abort_in_blackouts" in self.model_fields_set:
            _dict['abortInBlackouts'] = None

        # set to None if end_time_usecs (nullable) is None
        # and model_fields_set contains the field
        if self.end_time_usecs is None and "end_time_usecs" in self.model_fields_set:
            _dict['endTimeUsecs'] = None

        # set to None if policy_id (nullable) is None
        # and model_fields_set contains the field
        if self.policy_id is None and "policy_id" in self.model_fields_set:
            _dict['policyId'] = None

        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict['priority'] = None

        # set to None if qos_policy (nullable) is None
        # and model_fields_set contains the field
        if self.qos_policy is None and "qos_policy" in self.model_fields_set:
            _dict['qosPolicy'] = None

        # set to None if skip_rigel_for_backup (nullable) is None
        # and model_fields_set contains the field
        if self.skip_rigel_for_backup is None and "skip_rigel_for_backup" in self.model_fields_set:
            _dict['skipRigelForBackup'] = None

        # set to None if sla (nullable) is None
        # and model_fields_set contains the field
        if self.sla is None and "sla" in self.model_fields_set:
            _dict['sla'] = None

        # set to None if storage_domain_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_id is None and "storage_domain_id" in self.model_fields_set:
            _dict['storageDomainId'] = None

        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        # set to None if auto_protect_parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.auto_protect_parent_id is None and "auto_protect_parent_id" in self.model_fields_set:
            _dict['autoProtectParentId'] = None

        # set to None if is_active (nullable) is None
        # and model_fields_set contains the field
        if self.is_active is None and "is_active" in self.model_fields_set:
            _dict['isActive'] = None

        # set to None if is_auto_protect_config (nullable) is None
        # and model_fields_set contains the field
        if self.is_auto_protect_config is None and "is_auto_protect_config" in self.model_fields_set:
            _dict['isAutoProtectConfig'] = None

        # set to None if is_paused (nullable) is None
        # and model_fields_set contains the field
        if self.is_paused is None and "is_paused" in self.model_fields_set:
            _dict['isPaused'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProtectedObjectBackupConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "abortInBlackouts": obj.get("abortInBlackouts"),
            "endTimeUsecs": obj.get("endTimeUsecs"),
            "policyConfig": PolicyConfig.from_dict(obj["policyConfig"]) if obj.get("policyConfig") is not None else None,
            "policyId": obj.get("policyId"),
            "priority": obj.get("priority"),
            "qosPolicy": obj.get("qosPolicy"),
            "skipRigelForBackup": obj.get("skipRigelForBackup"),
            "sla": [SlaRule.from_dict(_item) for _item in obj["sla"]] if obj.get("sla") is not None else None,
            "startTime": TimeOfDay.from_dict(obj["startTime"]) if obj.get("startTime") is not None else None,
            "storageDomainId": obj.get("storageDomainId"),
            "awsParams": AwsObjectProtectionResponseParams.from_dict(obj["awsParams"]) if obj.get("awsParams") is not None else None,
            "azureParams": AzureObjectProtectionResponseParams.from_dict(obj["azureParams"]) if obj.get("azureParams") is not None else None,
            "elastifileParams": ElastifileObjectProtectionResponseParams.from_dict(obj["elastifileParams"]) if obj.get("elastifileParams") is not None else None,
            "environment": obj.get("environment"),
            "flashbladeParams": FlashbladeObjectProtectionResponseParams.from_dict(obj["flashbladeParams"]) if obj.get("flashbladeParams") is not None else None,
            "genericNasParams": GenericNasObjectProtectionResponseParams.from_dict(obj["genericNasParams"]) if obj.get("genericNasParams") is not None else None,
            "gpfsParams": GpfsObjectProtectionResponseParams.from_dict(obj["gpfsParams"]) if obj.get("gpfsParams") is not None else None,
            "hypervParams": HyperVObjectProtectionResponseParams.from_dict(obj["hypervParams"]) if obj.get("hypervParams") is not None else None,
            "isilonParams": IsilonObjectProtectionResponseParams.from_dict(obj["isilonParams"]) if obj.get("isilonParams") is not None else None,
            "mssqlParams": CommonMssqlObjectProtectionParams.from_dict(obj["mssqlParams"]) if obj.get("mssqlParams") is not None else None,
            "netappParams": NetappObjectProtectionResponseParams.from_dict(obj["netappParams"]) if obj.get("netappParams") is not None else None,
            "office365Params": Office365ObjectProtectionParams.from_dict(obj["office365Params"]) if obj.get("office365Params") is not None else None,
            "oracleParams": OracleObjectBasedProtectionParams.from_dict(obj["oracleParams"]) if obj.get("oracleParams") is not None else None,
            "physicalParams": PhysicalObjectProtectionParams.from_dict(obj["physicalParams"]) if obj.get("physicalParams") is not None else None,
            "sfdcParams": SfdcObjectProtectionParams.from_dict(obj["sfdcParams"]) if obj.get("sfdcParams") is not None else None,
            "udaParams": UdaObjectProtectionParams.from_dict(obj["udaParams"]) if obj.get("udaParams") is not None else None,
            "vmwareParams": VmwareObjectProtectionResponseParams.from_dict(obj["vmwareParams"]) if obj.get("vmwareParams") is not None else None,
            "autoProtectParentId": obj.get("autoProtectParentId"),
            "isActive": obj.get("isActive"),
            "isAutoProtectConfig": obj.get("isAutoProtectConfig"),
            "isPaused": obj.get("isPaused")
        })
        return _obj


