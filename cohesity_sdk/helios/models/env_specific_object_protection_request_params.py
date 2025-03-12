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
from cohesity_sdk.helios.models.aws_object_protection_request_params import AwsObjectProtectionRequestParams
from cohesity_sdk.helios.models.azure_object_protection_request_params import AzureObjectProtectionRequestParams
from cohesity_sdk.helios.models.elastifile_object_protection_request_params import ElastifileObjectProtectionRequestParams
from cohesity_sdk.helios.models.flashblade_object_protection_request_params import FlashbladeObjectProtectionRequestParams
from cohesity_sdk.helios.models.generic_nas_object_protection_request_params import GenericNasObjectProtectionRequestParams
from cohesity_sdk.helios.models.gpfs_object_protection_request_params import GpfsObjectProtectionRequestParams
from cohesity_sdk.helios.models.hyper_v_object_protection_request_params import HyperVObjectProtectionRequestParams
from cohesity_sdk.helios.models.isilon_object_protection_request_params import IsilonObjectProtectionRequestParams
from cohesity_sdk.helios.models.mssql_object_protection_params import MssqlObjectProtectionParams
from cohesity_sdk.helios.models.netapp_object_protection_request_params import NetappObjectProtectionRequestParams
from cohesity_sdk.helios.models.office365_object_protection_params import Office365ObjectProtectionParams
from cohesity_sdk.helios.models.oracle_object_based_protection_params import OracleObjectBasedProtectionParams
from cohesity_sdk.helios.models.physical_object_protection_params import PhysicalObjectProtectionParams
from cohesity_sdk.helios.models.sfdc_object_protection_params import SfdcObjectProtectionParams
from cohesity_sdk.helios.models.uda_object_protection_params import UdaObjectProtectionParams
from cohesity_sdk.helios.models.vmware_object_protection_request_params import VmwareObjectProtectionRequestParams
from typing import Optional, Set
from typing_extensions import Self

class EnvSpecificObjectProtectionRequestParams(BaseModel):
    """
    Specifies the parameters which are specific to adapter identified by environment.
    """ # noqa: E501
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the environment for current object.")
    aws_params: Optional[AwsObjectProtectionRequestParams] = Field(default=None, alias="awsParams")
    azure_params: Optional[AzureObjectProtectionRequestParams] = Field(default=None, alias="azureParams")
    elastifile_params: Optional[ElastifileObjectProtectionRequestParams] = Field(default=None, alias="elastifileParams")
    flashblade_params: Optional[FlashbladeObjectProtectionRequestParams] = Field(default=None, alias="flashbladeParams")
    generic_nas_params: Optional[GenericNasObjectProtectionRequestParams] = Field(default=None, alias="genericNasParams")
    gpfs_params: Optional[GpfsObjectProtectionRequestParams] = Field(default=None, alias="gpfsParams")
    hyperv_params: Optional[HyperVObjectProtectionRequestParams] = Field(default=None, alias="hypervParams")
    isilon_params: Optional[IsilonObjectProtectionRequestParams] = Field(default=None, alias="isilonParams")
    mssql_params: Optional[MssqlObjectProtectionParams] = Field(default=None, alias="mssqlParams")
    netapp_params: Optional[NetappObjectProtectionRequestParams] = Field(default=None, alias="netappParams")
    office365_params: Optional[Office365ObjectProtectionParams] = Field(default=None, alias="office365Params")
    oracle_params: Optional[OracleObjectBasedProtectionParams] = Field(default=None, alias="oracleParams")
    physical_params: Optional[PhysicalObjectProtectionParams] = Field(default=None, alias="physicalParams")
    sfdc_params: Optional[SfdcObjectProtectionParams] = Field(default=None, alias="sfdcParams")
    uda_params: Optional[UdaObjectProtectionParams] = Field(default=None, alias="udaParams")
    vmware_params: Optional[VmwareObjectProtectionRequestParams] = Field(default=None, alias="vmwareParams")
    __properties: ClassVar[List[str]] = ["environment", "awsParams", "azureParams", "elastifileParams", "flashbladeParams", "genericNasParams", "gpfsParams", "hypervParams", "isilonParams", "mssqlParams", "netappParams", "office365Params", "oracleParams", "physicalParams", "sfdcParams", "udaParams", "vmwareParams"]

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
        """Create an instance of EnvSpecificObjectProtectionRequestParams from a JSON string"""
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
        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnvSpecificObjectProtectionRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "environment": obj.get("environment"),
            "awsParams": AwsObjectProtectionRequestParams.from_dict(obj["awsParams"]) if obj.get("awsParams") is not None else None,
            "azureParams": AzureObjectProtectionRequestParams.from_dict(obj["azureParams"]) if obj.get("azureParams") is not None else None,
            "elastifileParams": ElastifileObjectProtectionRequestParams.from_dict(obj["elastifileParams"]) if obj.get("elastifileParams") is not None else None,
            "flashbladeParams": FlashbladeObjectProtectionRequestParams.from_dict(obj["flashbladeParams"]) if obj.get("flashbladeParams") is not None else None,
            "genericNasParams": GenericNasObjectProtectionRequestParams.from_dict(obj["genericNasParams"]) if obj.get("genericNasParams") is not None else None,
            "gpfsParams": GpfsObjectProtectionRequestParams.from_dict(obj["gpfsParams"]) if obj.get("gpfsParams") is not None else None,
            "hypervParams": HyperVObjectProtectionRequestParams.from_dict(obj["hypervParams"]) if obj.get("hypervParams") is not None else None,
            "isilonParams": IsilonObjectProtectionRequestParams.from_dict(obj["isilonParams"]) if obj.get("isilonParams") is not None else None,
            "mssqlParams": MssqlObjectProtectionParams.from_dict(obj["mssqlParams"]) if obj.get("mssqlParams") is not None else None,
            "netappParams": NetappObjectProtectionRequestParams.from_dict(obj["netappParams"]) if obj.get("netappParams") is not None else None,
            "office365Params": Office365ObjectProtectionParams.from_dict(obj["office365Params"]) if obj.get("office365Params") is not None else None,
            "oracleParams": OracleObjectBasedProtectionParams.from_dict(obj["oracleParams"]) if obj.get("oracleParams") is not None else None,
            "physicalParams": PhysicalObjectProtectionParams.from_dict(obj["physicalParams"]) if obj.get("physicalParams") is not None else None,
            "sfdcParams": SfdcObjectProtectionParams.from_dict(obj["sfdcParams"]) if obj.get("sfdcParams") is not None else None,
            "udaParams": UdaObjectProtectionParams.from_dict(obj["udaParams"]) if obj.get("udaParams") is not None else None,
            "vmwareParams": VmwareObjectProtectionRequestParams.from_dict(obj["vmwareParams"]) if obj.get("vmwareParams") is not None else None
        })
        return _obj


