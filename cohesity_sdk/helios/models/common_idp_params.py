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

class CommonIdpParams(BaseModel):
    """
    Specifies the Identity Provider Configuration.
    """ # noqa: E501
    certificate: Optional[StrictStr] = Field(description="Specifies the certificate generated for the app by the IdP service when the Helios is registered as an app. This is required to verify the SAML response.")
    default_clusters: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of default clusterIds assigned to an IdP user if clustersSamlAttributeName is not given. 'All' must be specified to give access to all clusters.", alias="defaultClusters")
    default_regions: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of default regionIds assigned to an IdP user if regionsSamlAttributeName is not given. 'All' must be specified to give access to all DataProtect as a Service regions.", alias="defaultRegions")
    default_roles: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of default roles assigned to an IdP user if rolesSamlAttributeName is not given.", alias="defaultRoles")
    domain: Optional[StrictStr] = Field(description="Specifies a unique name for this IdP configuration.")
    is_enabled: Optional[StrictBool] = Field(default=None, description="Specifies a flag to enable or disable this IdP service. When it is set to true, IdP service is enabled. When it is set to false, IdP service is disabled. Default value is true.", alias="isEnabled")
    issuer_id: Optional[StrictStr] = Field(description="Specifies the IdP provided Issuer ID for the app. For example, exkh1aov1nhHrgFhN0h7.", alias="issuerId")
    name: Optional[StrictStr] = Field(description="Specifies the name of the vendor providing IDP service.")
    sf_account_id: Optional[StrictStr] = Field(default=None, description="Specifies the salesforce account ID linked to this IDP. Either of TenantId or SfAccountId would be set for IdP.", alias="sfAccountId")
    sign_request: Optional[StrictBool] = Field(default=None, description="Specifies whether to sign the SAML request or not. When it is set to true, SAML request will be signed. When it is set to false, SAML request is not signed. Default is false. Set this flag to true if the IdP site is configured to expect the SAML request from Helios signed. If this is set to true, users must get the Helios certificate and upload it on the IdP site.", alias="signRequest")
    sso_url: Optional[StrictStr] = Field(description="Specifies the SSO URL of the IdP service for the customer. This is the URL given by IdP when the customer created an account. For example, dev-332534.oktapreview.com.", alias="ssoUrl")
    tenant_id: Optional[StrictStr] = Field(default=None, description="Specifies the Tenant Id if the IdP is configured for a Tenant. Either of TenantId or SfAccountId would be set for IdP.", alias="tenantId")
    __properties: ClassVar[List[str]] = ["certificate", "defaultClusters", "defaultRegions", "defaultRoles", "domain", "isEnabled", "issuerId", "name", "sfAccountId", "signRequest", "ssoUrl", "tenantId"]

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
        """Create an instance of CommonIdpParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "sf_account_id",
            "tenant_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if certificate (nullable) is None
        # and model_fields_set contains the field
        if self.certificate is None and "certificate" in self.model_fields_set:
            _dict['certificate'] = None

        # set to None if default_clusters (nullable) is None
        # and model_fields_set contains the field
        if self.default_clusters is None and "default_clusters" in self.model_fields_set:
            _dict['defaultClusters'] = None

        # set to None if default_regions (nullable) is None
        # and model_fields_set contains the field
        if self.default_regions is None and "default_regions" in self.model_fields_set:
            _dict['defaultRegions'] = None

        # set to None if default_roles (nullable) is None
        # and model_fields_set contains the field
        if self.default_roles is None and "default_roles" in self.model_fields_set:
            _dict['defaultRoles'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if is_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.is_enabled is None and "is_enabled" in self.model_fields_set:
            _dict['isEnabled'] = None

        # set to None if issuer_id (nullable) is None
        # and model_fields_set contains the field
        if self.issuer_id is None and "issuer_id" in self.model_fields_set:
            _dict['issuerId'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if sf_account_id (nullable) is None
        # and model_fields_set contains the field
        if self.sf_account_id is None and "sf_account_id" in self.model_fields_set:
            _dict['sfAccountId'] = None

        # set to None if sign_request (nullable) is None
        # and model_fields_set contains the field
        if self.sign_request is None and "sign_request" in self.model_fields_set:
            _dict['signRequest'] = None

        # set to None if sso_url (nullable) is None
        # and model_fields_set contains the field
        if self.sso_url is None and "sso_url" in self.model_fields_set:
            _dict['ssoUrl'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonIdpParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "certificate": obj.get("certificate"),
            "defaultClusters": obj.get("defaultClusters"),
            "defaultRegions": obj.get("defaultRegions"),
            "defaultRoles": obj.get("defaultRoles"),
            "domain": obj.get("domain"),
            "isEnabled": obj.get("isEnabled"),
            "issuerId": obj.get("issuerId"),
            "name": obj.get("name"),
            "sfAccountId": obj.get("sfAccountId"),
            "signRequest": obj.get("signRequest"),
            "ssoUrl": obj.get("ssoUrl"),
            "tenantId": obj.get("tenantId")
        })
        return _obj


