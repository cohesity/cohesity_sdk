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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.aws_kms_configuration_update_params import AwsKmsConfigurationUpdateParams
from cohesity_sdk.cluster.models.kmip_kms_configuration import KmipKmsConfiguration
from typing import Set
from typing_extensions import Self

class KmsConfigurationUpdateParams(BaseModel):
    """
    Parameters to update key management system(KMS) on the cluster.
    """ # noqa: E501
    external_target_ids: Optional[List[StrictInt]] = Field(default=None, description="Ids of external targets used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to an external target, it cannot be changed.", alias="externalTargetIds")
    kmip_kms_params: Optional[KmipKmsConfiguration] = Field(default=None, alias="kmipKmsParams")
    name: StrictStr = Field(description="Name of the KMS.")
    storage_domain_ids: Optional[List[StrictInt]] = Field(default=None, description="Ids of storage domains used to assign the KMS for encryption. Once an external KMS (AWS KMS or KIMP KMS) is assigned to a storage domain, it cannot be changed.", alias="storageDomainIds")
    aws_kms_params: Optional[AwsKmsConfigurationUpdateParams] = Field(default=None, alias="awsKmsParams")
    __properties: ClassVar[List[str]] = ["externalTargetIds", "kmipKmsParams", "name", "storageDomainIds", "awsKmsParams"]

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
        """Create an instance of KmsConfigurationUpdateParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of kmip_kms_params
        if self.kmip_kms_params:
            _dict['kmipKmsParams'] = self.kmip_kms_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aws_kms_params
        if self.aws_kms_params:
            _dict['awsKmsParams'] = self.aws_kms_params.to_dict()
        # set to None if external_target_ids (nullable) is None
        # and model_fields_set contains the field
        if self.external_target_ids is None and "external_target_ids" in self.model_fields_set:
            _dict['externalTargetIds'] = None

        # set to None if storage_domain_ids (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_ids is None and "storage_domain_ids" in self.model_fields_set:
            _dict['storageDomainIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KmsConfigurationUpdateParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "externalTargetIds": obj.get("externalTargetIds"),
            "kmipKmsParams": KmipKmsConfiguration.from_dict(obj["kmipKmsParams"]) if obj.get("kmipKmsParams") is not None else None,
            "name": obj.get("name"),
            "storageDomainIds": obj.get("storageDomainIds"),
            "awsKmsParams": AwsKmsConfigurationUpdateParams.from_dict(obj["awsKmsParams"]) if obj.get("awsKmsParams") is not None else None
        })
        return _obj


