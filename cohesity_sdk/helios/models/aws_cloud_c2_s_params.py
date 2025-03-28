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

class AwsCloudC2SParams(BaseModel):
    """
    Specifies the parameters which are specific to AWS related External Targets with Cloud Type C2S.
    """ # noqa: E501
    agency: Optional[StrictStr] = Field(description="Specifies agency of the External Target.")
    base_url: Optional[StrictStr] = Field(description="Specifies base url of the External Target.", alias="baseURL")
    client_certificate: Optional[StrictStr] = Field(description="Specifies client certificate of the External Target", alias="clientCertificate")
    client_certificate_password: Optional[StrictStr] = Field(description="Specifies client certificate password of the External Target", alias="clientCertificatePassword")
    client_private_key: Optional[StrictStr] = Field(description="Specifies client private key of the External Target", alias="clientPrivateKey")
    mission: Optional[StrictStr] = Field(description="Specifies mission of the External Target")
    role: Optional[StrictStr] = Field(description="Specifies role of the External Target")
    server_ca_trusted_certificate: Optional[StrictStr] = Field(description="Specifies server CA trusted certificate of the External Target", alias="serverCATrustedCertificate")
    __properties: ClassVar[List[str]] = ["agency", "baseURL", "clientCertificate", "clientCertificatePassword", "clientPrivateKey", "mission", "role", "serverCATrustedCertificate"]

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
        """Create an instance of AwsCloudC2SParams from a JSON string"""
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
        # set to None if agency (nullable) is None
        # and model_fields_set contains the field
        if self.agency is None and "agency" in self.model_fields_set:
            _dict['agency'] = None

        # set to None if base_url (nullable) is None
        # and model_fields_set contains the field
        if self.base_url is None and "base_url" in self.model_fields_set:
            _dict['baseURL'] = None

        # set to None if client_certificate (nullable) is None
        # and model_fields_set contains the field
        if self.client_certificate is None and "client_certificate" in self.model_fields_set:
            _dict['clientCertificate'] = None

        # set to None if client_certificate_password (nullable) is None
        # and model_fields_set contains the field
        if self.client_certificate_password is None and "client_certificate_password" in self.model_fields_set:
            _dict['clientCertificatePassword'] = None

        # set to None if client_private_key (nullable) is None
        # and model_fields_set contains the field
        if self.client_private_key is None and "client_private_key" in self.model_fields_set:
            _dict['clientPrivateKey'] = None

        # set to None if mission (nullable) is None
        # and model_fields_set contains the field
        if self.mission is None and "mission" in self.model_fields_set:
            _dict['mission'] = None

        # set to None if role (nullable) is None
        # and model_fields_set contains the field
        if self.role is None and "role" in self.model_fields_set:
            _dict['role'] = None

        # set to None if server_ca_trusted_certificate (nullable) is None
        # and model_fields_set contains the field
        if self.server_ca_trusted_certificate is None and "server_ca_trusted_certificate" in self.model_fields_set:
            _dict['serverCATrustedCertificate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsCloudC2SParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agency": obj.get("agency"),
            "baseURL": obj.get("baseURL"),
            "clientCertificate": obj.get("clientCertificate"),
            "clientCertificatePassword": obj.get("clientCertificatePassword"),
            "clientPrivateKey": obj.get("clientPrivateKey"),
            "mission": obj.get("mission"),
            "role": obj.get("role"),
            "serverCATrustedCertificate": obj.get("serverCATrustedCertificate")
        })
        return _obj


