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
from cohesity_sdk.helios.models.common_protection_group_run_response_parameters import CommonProtectionGroupRunResponseParameters
from typing import Optional, Set
from typing_extensions import Self

class ProtectionGroupInfo(BaseModel):
    """
    Specifies basic information about a Protection Group.
    """ # noqa: E501
    group_id: Optional[StrictInt] = Field(default=None, description="This field is deprecated. 'protectionGroupId' should be used instead. Specifies the id of the Protection Group.", alias="groupId")
    group_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the Protection Group.", alias="groupName")
    is_paused: Optional[StrictBool] = Field(default=None, description="Specifies if the Protection Group's run is paused.", alias="isPaused")
    last_run: Optional[CommonProtectionGroupRunResponseParameters] = Field(default=None, alias="lastRun")
    protection_group_id: Optional[StrictStr] = Field(default=None, description="Specifies the protection group id.", alias="protectionGroupId")
    type: Optional[StrictStr] = Field(default=None, description="Specifies the type of the Protection Group such as View or Puppeteer. 'Puppeteer' refers to a Remote Adapter Group. Supported environment types such as 'View', 'SQL', 'VMware', etc. NOTE: 'Puppeteer' refers to Cohesity's Remote Adapter. 'VMware' indicates the VMware Protection Source environment. 'HyperV' indicates the HyperV Protection Source environment. 'SQL' indicates the SQL Protection Source environment. 'View' indicates the View Protection Source environment. 'Puppeteer' indicates the Cohesity's Remote Adapter. 'Physical' indicates the physical Protection Source environment. 'Pure' indicates the Pure Storage Protection Source environment. 'Nimble' indicates the Nimble Storage Protection Source environment. 'Azure' indicates the Microsoft's Azure Protection Source environment. 'Netapp' indicates the Netapp Protection Source environment. 'Agent' indicates the Agent Protection Source environment. 'GenericNas' indicates the Generic Network Attached Storage Protection Source environment. 'Acropolis' indicates the Acropolis Protection Source environment. 'PhsicalFiles' indicates the Physical Files Protection Source environment. 'Isilon' indicates the Dell EMC's Isilon Protection Source environment. 'GPFS' indicates IBM's GPFS Protection Source environment. 'KVM' indicates the KVM Protection Source environment. 'AWS' indicates the AWS Protection Source environment. 'Exchange' indicates the Exchange Protection Source environment. 'HyperVVSS' indicates the HyperV VSS Protection Source environment. 'Oracle' indicates the Oracle Protection Source environment. 'GCP' indicates the Google Cloud Platform Protection Source environment. 'FlashBlade' indicates the Flash Blade Protection Source environment. 'AWSNative' indicates the AWS Native Protection Source environment. 'O365' indicates the Office 365 Protection Source environment. 'O365Outlook' indicates Office 365 outlook Protection Source environment. 'HyperFlex' indicates the Hyper Flex Protection Source environment. 'GCPNative' indicates the GCP Native Protection Source environment. 'AzureNative' indicates the Azure Native Protection Source environment. 'Kubernetes' indicates a Kubernetes Protection Source environment. 'Elastifile' indicates Elastifile Protection Source environment. 'AD' indicates Active Directory Protection Source environment.")
    __properties: ClassVar[List[str]] = ["groupId", "groupName", "isPaused", "lastRun", "protectionGroupId", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kVCD', 'kSQL', 'kView', 'kRemoteAdapter', 'kPhysical', 'kPure', 'kIbmFlashSystem', 'kAzure', 'kNetapp', 'kGenericNas', 'kAcropolis', 'kIsilon', 'kKVM', 'kAWS', 'kAWSNative', 'kAwsS3', 'kAWSSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSQL', 'kAzureSnapshotManager', 'kExchange', 'kOracle', 'kGCP', 'kFlashBlade', 'kO365', 'kHyperFlex', 'kAD', 'kGPFS', 'kKubernetes', 'kNimble', 'kElastifile', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kO365Sharepoint', 'kO365PublicFolders', 'kO365Teams', 'kO365Group', 'kO365Exchange', 'kO365OneDrive', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kVCD', 'kSQL', 'kView', 'kRemoteAdapter', 'kPhysical', 'kPure', 'kIbmFlashSystem', 'kAzure', 'kNetapp', 'kGenericNas', 'kAcropolis', 'kIsilon', 'kKVM', 'kAWS', 'kAWSNative', 'kAwsS3', 'kAWSSnapshotManager', 'kRDSSnapshotManager', 'kAuroraSnapshotManager', 'kAwsRDSPostgresBackup', 'kAzureNative', 'kAzureSQL', 'kAzureSnapshotManager', 'kExchange', 'kOracle', 'kGCP', 'kFlashBlade', 'kO365', 'kHyperFlex', 'kAD', 'kGPFS', 'kKubernetes', 'kNimble', 'kElastifile', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kO365Sharepoint', 'kO365PublicFolders', 'kO365Teams', 'kO365Group', 'kO365Exchange', 'kO365OneDrive', 'kSfdc')")
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
        """Create an instance of ProtectionGroupInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of last_run
        if self.last_run:
            _dict['lastRun'] = self.last_run.to_dict()
        # set to None if group_id (nullable) is None
        # and model_fields_set contains the field
        if self.group_id is None and "group_id" in self.model_fields_set:
            _dict['groupId'] = None

        # set to None if group_name (nullable) is None
        # and model_fields_set contains the field
        if self.group_name is None and "group_name" in self.model_fields_set:
            _dict['groupName'] = None

        # set to None if is_paused (nullable) is None
        # and model_fields_set contains the field
        if self.is_paused is None and "is_paused" in self.model_fields_set:
            _dict['isPaused'] = None

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProtectionGroupInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "groupId": obj.get("groupId"),
            "groupName": obj.get("groupName"),
            "isPaused": obj.get("isPaused"),
            "lastRun": CommonProtectionGroupRunResponseParameters.from_dict(obj["lastRun"]) if obj.get("lastRun") is not None else None,
            "protectionGroupId": obj.get("protectionGroupId"),
            "type": obj.get("type")
        })
        return _obj


