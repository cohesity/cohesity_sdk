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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class CreateIdpRequestParams(BaseModel):
    """
    Specifies parameters to configure identity provider
    """ # noqa: E501
    allow_local_user_login: Optional[StrictBool] = Field(default=None, description="Specifies if local user login is allowed. When idp is configured, only idp users are allowed to login to the cluster, local login is disabled except for users with admin role. If this flag is set to true, local (non-idp) logins are allowed for all local and AD users. Local or AD users with admin role can login always independent of this flag's setting. By default there is no local authentication i.e the value is false.", alias="allowLocalUserLogin")
    certificate: Optional[StrictStr] = Field(description="Specifies the certificate generated for the app by the idp service when the cluster is registered as an app. This is required to verify the SAML response.")
    certificate_filename: Optional[StrictStr] = Field(default=None, description="Specifies the filename used for the certificate. The default value is idp_certificate.pem", alias="certificateFilename")
    is_enabled: Optional[StrictBool] = Field(default=None, description="Specifies a flag to enable or disable this idp service. When it is set to true, idp service is enabled. When it is set to false, idp service is disabled. By defaut idp is enabled i.e the value is true.", alias="isEnabled")
    issuer_id: Optional[StrictStr] = Field(description="Specifies identity provider issuer id", alias="issuerId")
    roles: Optional[List[StrictStr]] = Field(default=None, description="Specifies the default roles assined for all SSO users")
    saml_attribute_name: Optional[StrictStr] = Field(default=None, description="Specifies the SAML attribute name that contains a comma separated list of cluster roles. This sets the default roles for all SSO users. Either this field or roles must be set, this field takes higher precedence than the roles field.", alias="samlAttributeName")
    sign_request: Optional[StrictBool] = Field(default=None, description="Specifies whether to sign the SAML request or not. When it is set to true, SAML request will be signed. When it is set to false, SAML request is not signed. Default is false, set this flag to true if the idp site is configured to expect the SAML request from the Cluster signed. If this is set to true, users must get the cluster's certificate and upload it on the idp site.", alias="signRequest")
    sso_url: Optional[StrictStr] = Field(description="Specifies the identity provider SSO url", alias="ssoUrl")
    domain: Optional[StrictStr] = Field(description="Specifies domain of idp configuration")
    name: Optional[StrictStr] = Field(description="Specifies name of the vendor providing idp service")
    tenant_id: Optional[StrictStr] = Field(default=None, description="Specifies the tenant id if the idp is configured for a tenant. If this is not set, this idp configuration is used for the cluster level users and for all users of tenants not having an idp configuration.", alias="tenantId")
    __properties: ClassVar[List[str]] = ["allowLocalUserLogin", "certificate", "certificateFilename", "isEnabled", "issuerId", "roles", "samlAttributeName", "signRequest", "ssoUrl", "domain", "name", "tenantId"]

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
        """Create an instance of CreateIdpRequestParams from a JSON string"""
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
        # set to None if allow_local_user_login (nullable) is None
        # and model_fields_set contains the field
        if self.allow_local_user_login is None and "allow_local_user_login" in self.model_fields_set:
            _dict['allowLocalUserLogin'] = None

        # set to None if certificate (nullable) is None
        # and model_fields_set contains the field
        if self.certificate is None and "certificate" in self.model_fields_set:
            _dict['certificate'] = None

        # set to None if certificate_filename (nullable) is None
        # and model_fields_set contains the field
        if self.certificate_filename is None and "certificate_filename" in self.model_fields_set:
            _dict['certificateFilename'] = None

        # set to None if is_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.is_enabled is None and "is_enabled" in self.model_fields_set:
            _dict['isEnabled'] = None

        # set to None if issuer_id (nullable) is None
        # and model_fields_set contains the field
        if self.issuer_id is None and "issuer_id" in self.model_fields_set:
            _dict['issuerId'] = None

        # set to None if roles (nullable) is None
        # and model_fields_set contains the field
        if self.roles is None and "roles" in self.model_fields_set:
            _dict['roles'] = None

        # set to None if saml_attribute_name (nullable) is None
        # and model_fields_set contains the field
        if self.saml_attribute_name is None and "saml_attribute_name" in self.model_fields_set:
            _dict['samlAttributeName'] = None

        # set to None if sign_request (nullable) is None
        # and model_fields_set contains the field
        if self.sign_request is None and "sign_request" in self.model_fields_set:
            _dict['signRequest'] = None

        # set to None if sso_url (nullable) is None
        # and model_fields_set contains the field
        if self.sso_url is None and "sso_url" in self.model_fields_set:
            _dict['ssoUrl'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateIdpRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowLocalUserLogin": obj.get("allowLocalUserLogin"),
            "certificate": obj.get("certificate"),
            "certificateFilename": obj.get("certificateFilename"),
            "isEnabled": obj.get("isEnabled"),
            "issuerId": obj.get("issuerId"),
            "roles": obj.get("roles"),
            "samlAttributeName": obj.get("samlAttributeName"),
            "signRequest": obj.get("signRequest"),
            "ssoUrl": obj.get("ssoUrl"),
            "domain": obj.get("domain"),
            "name": obj.get("name"),
            "tenantId": obj.get("tenantId")
        })
        return _obj


