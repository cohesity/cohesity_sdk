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
from typing import Set
from typing_extensions import Self

class CommonGcpExternalTargetParams(BaseModel):
    """
    Specifies the common parameters which are specific to GCP related External Targets.
    """ # noqa: E501
    bucket_name: Optional[StrictStr] = Field(description="Specifies the bucket name of the external target.", alias="bucketName")
    client_email_address: Optional[StrictStr] = Field(description="Specifies the client email address of the external target.", alias="clientEmailAddress")
    client_private_key: Optional[StrictStr] = Field(default=None, description="Specifies the client private key of the external target.", alias="clientPrivateKey")
    project_id: Optional[StrictStr] = Field(description="Specifies the project Id of the external target.", alias="projectId")
    __properties: ClassVar[List[str]] = ["bucketName", "clientEmailAddress", "clientPrivateKey", "projectId"]

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
        """Create an instance of CommonGcpExternalTargetParams from a JSON string"""
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
        # set to None if bucket_name (nullable) is None
        # and model_fields_set contains the field
        if self.bucket_name is None and "bucket_name" in self.model_fields_set:
            _dict['bucketName'] = None

        # set to None if client_email_address (nullable) is None
        # and model_fields_set contains the field
        if self.client_email_address is None and "client_email_address" in self.model_fields_set:
            _dict['clientEmailAddress'] = None

        # set to None if client_private_key (nullable) is None
        # and model_fields_set contains the field
        if self.client_private_key is None and "client_private_key" in self.model_fields_set:
            _dict['clientPrivateKey'] = None

        # set to None if project_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_id is None and "project_id" in self.model_fields_set:
            _dict['projectId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonGcpExternalTargetParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bucketName": obj.get("bucketName"),
            "clientEmailAddress": obj.get("clientEmailAddress"),
            "clientPrivateKey": obj.get("clientPrivateKey"),
            "projectId": obj.get("projectId")
        })
        return _obj


