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
from cohesity_sdk.helios.models.kms_key_basic_info import KmsKeyBasicInfo
from cohesity_sdk.helios.models.provision_status import ProvisionStatus
from cohesity_sdk.helios.models.rpaas_pairing_info import RpaasPairingInfo
from typing import Set
from typing_extensions import Self

class RpaasRegionInfo(BaseModel):
    """
    Specifies a Rpaas enabled region.
    """ # noqa: E501
    bucket_name: Optional[StrictStr] = Field(default=None, description="Name of the S3 bucket.", alias="bucketName")
    global_vault_id: Optional[StrictStr] = Field(default=None, description="Global vault ID.", alias="globalVaultId")
    kms_key_info: Optional[KmsKeyBasicInfo] = Field(default=None, alias="kmsKeyInfo")
    pairing_info: Optional[List[RpaasPairingInfo]] = Field(default=None, description="The configured cluster for the particular region.", alias="pairingInfo")
    provision_status: Optional[ProvisionStatus] = Field(default=None, alias="provisionStatus")
    region_id: Optional[StrictStr] = Field(default=None, description="ID that identifies a region.", alias="regionId")
    region_name: Optional[StrictStr] = Field(default=None, description="Name of the region.", alias="regionName")
    region_provision_type: Optional[StrictStr] = Field(default=None, description="Indicates whether the tenant type is Cohesity KMS or Customer managed KMS.", alias="regionProvisionType")
    storage_class: Optional[StrictStr] = Field(default=None, description="Specifies the AWS storage class.", alias="storageClass")
    vault_name: Optional[StrictStr] = Field(default=None, description="Name of the vault.", alias="vaultName")
    __properties: ClassVar[List[str]] = ["bucketName", "globalVaultId", "kmsKeyInfo", "pairingInfo", "provisionStatus", "regionId", "regionName", "regionProvisionType", "storageClass", "vaultName"]

    @field_validator('region_id')
    def region_id_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1', 'ap-northeast-1', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'eu-west-2', 'me-south-1', 'eu-west-3']):
            raise ValueError("must be one of enum values ('us-east-1', 'us-east-2', 'us-west-1', 'us-west-2', 'ca-central-1', 'ap-northeast-1', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'eu-central-1', 'eu-west-2', 'me-south-1', 'eu-west-3')")
        return value

    @field_validator('region_provision_type')
    def region_provision_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Cohesity', 'CustomerManaged']):
            raise ValueError("must be one of enum values ('Cohesity', 'CustomerManaged')")
        return value

    @field_validator('storage_class')
    def storage_class_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kAmazonS3StandardIA', 'kAmazonS3Glacier']):
            raise ValueError("must be one of enum values ('kAmazonS3StandardIA', 'kAmazonS3Glacier')")
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
        """Create an instance of RpaasRegionInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of kms_key_info
        if self.kms_key_info:
            _dict['kmsKeyInfo'] = self.kms_key_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pairing_info (list)
        _items = []
        if self.pairing_info:
            for _item_pairing_info in self.pairing_info:
                if _item_pairing_info:
                    _items.append(_item_pairing_info.to_dict())
            _dict['pairingInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of provision_status
        if self.provision_status:
            _dict['provisionStatus'] = self.provision_status.to_dict()
        # set to None if bucket_name (nullable) is None
        # and model_fields_set contains the field
        if self.bucket_name is None and "bucket_name" in self.model_fields_set:
            _dict['bucketName'] = None

        # set to None if global_vault_id (nullable) is None
        # and model_fields_set contains the field
        if self.global_vault_id is None and "global_vault_id" in self.model_fields_set:
            _dict['globalVaultId'] = None

        # set to None if pairing_info (nullable) is None
        # and model_fields_set contains the field
        if self.pairing_info is None and "pairing_info" in self.model_fields_set:
            _dict['pairingInfo'] = None

        # set to None if region_id (nullable) is None
        # and model_fields_set contains the field
        if self.region_id is None and "region_id" in self.model_fields_set:
            _dict['regionId'] = None

        # set to None if region_name (nullable) is None
        # and model_fields_set contains the field
        if self.region_name is None and "region_name" in self.model_fields_set:
            _dict['regionName'] = None

        # set to None if region_provision_type (nullable) is None
        # and model_fields_set contains the field
        if self.region_provision_type is None and "region_provision_type" in self.model_fields_set:
            _dict['regionProvisionType'] = None

        # set to None if storage_class (nullable) is None
        # and model_fields_set contains the field
        if self.storage_class is None and "storage_class" in self.model_fields_set:
            _dict['storageClass'] = None

        # set to None if vault_name (nullable) is None
        # and model_fields_set contains the field
        if self.vault_name is None and "vault_name" in self.model_fields_set:
            _dict['vaultName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RpaasRegionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bucketName": obj.get("bucketName"),
            "globalVaultId": obj.get("globalVaultId"),
            "kmsKeyInfo": KmsKeyBasicInfo.from_dict(obj["kmsKeyInfo"]) if obj.get("kmsKeyInfo") is not None else None,
            "pairingInfo": [RpaasPairingInfo.from_dict(_item) for _item in obj["pairingInfo"]] if obj.get("pairingInfo") is not None else None,
            "provisionStatus": ProvisionStatus.from_dict(obj["provisionStatus"]) if obj.get("provisionStatus") is not None else None,
            "regionId": obj.get("regionId"),
            "regionName": obj.get("regionName"),
            "regionProvisionType": obj.get("regionProvisionType"),
            "storageClass": obj.get("storageClass"),
            "vaultName": obj.get("vaultName")
        })
        return _obj


