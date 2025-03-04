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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CommonOracleExternalTargetParams(BaseModel):
    """
    Specifies the common parameters which are specific to Oracle related External Targets.
    """ # noqa: E501
    access_key_id: Optional[StrictStr] = Field(description="Specifies the access key id of the external target.", alias="accessKeyId")
    bucket_name: Optional[StrictStr] = Field(description="Specifies the bucket name of the external target.", alias="bucketName")
    region: Optional[StrictStr] = Field(description="Specifies the region of the external target.")
    storage_access_key: Optional[StrictStr] = Field(default=None, description="Specifies the storage access key of the external target.", alias="storageAccessKey")
    tenancy: Optional[StrictStr] = Field(description="Specifies the tenancy of the external target.")
    __properties: ClassVar[List[str]] = ["accessKeyId", "bucketName", "region", "storageAccessKey", "tenancy"]

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
        """Create an instance of CommonOracleExternalTargetParams from a JSON string"""
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
        # set to None if access_key_id (nullable) is None
        # and model_fields_set contains the field
        if self.access_key_id is None and "access_key_id" in self.model_fields_set:
            _dict['accessKeyId'] = None

        # set to None if bucket_name (nullable) is None
        # and model_fields_set contains the field
        if self.bucket_name is None and "bucket_name" in self.model_fields_set:
            _dict['bucketName'] = None

        # set to None if region (nullable) is None
        # and model_fields_set contains the field
        if self.region is None and "region" in self.model_fields_set:
            _dict['region'] = None

        # set to None if storage_access_key (nullable) is None
        # and model_fields_set contains the field
        if self.storage_access_key is None and "storage_access_key" in self.model_fields_set:
            _dict['storageAccessKey'] = None

        # set to None if tenancy (nullable) is None
        # and model_fields_set contains the field
        if self.tenancy is None and "tenancy" in self.model_fields_set:
            _dict['tenancy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonOracleExternalTargetParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessKeyId": obj.get("accessKeyId"),
            "bucketName": obj.get("bucketName"),
            "region": obj.get("region"),
            "storageAccessKey": obj.get("storageAccessKey"),
            "tenancy": obj.get("tenancy")
        })
        return _obj


