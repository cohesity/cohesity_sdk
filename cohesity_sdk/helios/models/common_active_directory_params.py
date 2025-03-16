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
from typing_extensions import Annotated
from cohesity_sdk.helios.models.domain_controller import DomainController
from cohesity_sdk.helios.models.machine_account import MachineAccount
from cohesity_sdk.helios.models.trusted_domain_params import TrustedDomainParams
from typing import Optional, Set
from typing_extensions import Self

class CommonActiveDirectoryParams(BaseModel):
    """
    Specifies the params of Active Directory which are used across creating and updating.
    """ # noqa: E501
    connection_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the connection.", alias="connectionId")
    domain_controllers_deny_list: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Specifies a list of denied domain controllers of this Active Directory Domain.", alias="domainControllersDenyList")
    id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the Active Directory.")
    ldap_provider_id: Optional[StrictInt] = Field(default=None, description="Specifies the LDAP provider id which is mapped to this Active Directory", alias="ldapProviderId")
    machine_accounts: Optional[Annotated[List[MachineAccount], Field(min_length=1)]] = Field(description="Specifies a list of computer names used to identify the Cohesity Cluster on the Active Directory domain. The first machine account is used as primary machine account and it can not be modified.", alias="machineAccounts")
    nis_provider_domain_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the NIS Provider which is mapped to this Active Directory.", alias="nisProviderDomainName")
    organizational_unit_name: Optional[StrictStr] = Field(default=None, description="Specifies an optional organizational unit name.", alias="organizationalUnitName")
    preferred_domain_controllers: Optional[List[DomainController]] = Field(default=None, description="Specifies a list of preferred domain controllers of this Active Directory.", alias="preferredDomainControllers")
    trusted_domain_params: Optional[TrustedDomainParams] = Field(default=None, description="Specifies the params of trusted domain info of an Active Directory.", alias="trustedDomainParams")
    work_group_name: Optional[StrictStr] = Field(default=None, description="Specifies a work group name.", alias="workGroupName")
    __properties: ClassVar[List[str]] = ["connectionId", "domainControllersDenyList", "id", "ldapProviderId", "machineAccounts", "nisProviderDomainName", "organizationalUnitName", "preferredDomainControllers", "trustedDomainParams", "workGroupName"]

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
        """Create an instance of CommonActiveDirectoryParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in machine_accounts (list)
        _items = []
        if self.machine_accounts:
            for _item_machine_accounts in self.machine_accounts:
                if _item_machine_accounts:
                    _items.append(_item_machine_accounts.to_dict())
            _dict['machineAccounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in preferred_domain_controllers (list)
        _items = []
        if self.preferred_domain_controllers:
            for _item_preferred_domain_controllers in self.preferred_domain_controllers:
                if _item_preferred_domain_controllers:
                    _items.append(_item_preferred_domain_controllers.to_dict())
            _dict['preferredDomainControllers'] = _items
        # override the default output from pydantic by calling `to_dict()` of trusted_domain_params
        if self.trusted_domain_params:
            _dict['trustedDomainParams'] = self.trusted_domain_params.to_dict()
        # set to None if connection_id (nullable) is None
        # and model_fields_set contains the field
        if self.connection_id is None and "connection_id" in self.model_fields_set:
            _dict['connectionId'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if ldap_provider_id (nullable) is None
        # and model_fields_set contains the field
        if self.ldap_provider_id is None and "ldap_provider_id" in self.model_fields_set:
            _dict['ldapProviderId'] = None

        # set to None if machine_accounts (nullable) is None
        # and model_fields_set contains the field
        if self.machine_accounts is None and "machine_accounts" in self.model_fields_set:
            _dict['machineAccounts'] = None

        # set to None if nis_provider_domain_name (nullable) is None
        # and model_fields_set contains the field
        if self.nis_provider_domain_name is None and "nis_provider_domain_name" in self.model_fields_set:
            _dict['nisProviderDomainName'] = None

        # set to None if organizational_unit_name (nullable) is None
        # and model_fields_set contains the field
        if self.organizational_unit_name is None and "organizational_unit_name" in self.model_fields_set:
            _dict['organizationalUnitName'] = None

        # set to None if preferred_domain_controllers (nullable) is None
        # and model_fields_set contains the field
        if self.preferred_domain_controllers is None and "preferred_domain_controllers" in self.model_fields_set:
            _dict['preferredDomainControllers'] = None

        # set to None if trusted_domain_params (nullable) is None
        # and model_fields_set contains the field
        if self.trusted_domain_params is None and "trusted_domain_params" in self.model_fields_set:
            _dict['trustedDomainParams'] = None

        # set to None if work_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.work_group_name is None and "work_group_name" in self.model_fields_set:
            _dict['workGroupName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommonActiveDirectoryParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "connectionId": obj.get("connectionId"),
            "domainControllersDenyList": obj.get("domainControllersDenyList"),
            "id": obj.get("id"),
            "ldapProviderId": obj.get("ldapProviderId"),
            "machineAccounts": [MachineAccount.from_dict(_item) for _item in obj["machineAccounts"]] if obj.get("machineAccounts") is not None else None,
            "nisProviderDomainName": obj.get("nisProviderDomainName"),
            "organizationalUnitName": obj.get("organizationalUnitName"),
            "preferredDomainControllers": [DomainController.from_dict(_item) for _item in obj["preferredDomainControllers"]] if obj.get("preferredDomainControllers") is not None else None,
            "trustedDomainParams": TrustedDomainParams.from_dict(obj["trustedDomainParams"]) if obj.get("trustedDomainParams") is not None else None,
            "workGroupName": obj.get("workGroupName")
        })
        return _obj


