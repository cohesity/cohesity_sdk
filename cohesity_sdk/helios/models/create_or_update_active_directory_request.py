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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.helios.models.domain_controller import DomainController
from cohesity_sdk.helios.models.mcm_machine_account import McmMachineAccount
from cohesity_sdk.helios.models.trusted_domain_info import TrustedDomainInfo
from cohesity_sdk.helios.models.trusted_domain_params import TrustedDomainParams
from typing import Set
from typing_extensions import Self

class CreateOrUpdateActiveDirectoryRequest(BaseModel):
    """
    Specifies the request to create an Active Directory.
    """ # noqa: E501
    domain_name: Optional[Annotated[str, Field(strict=True)]] = Field(description="Specifies the domain name of the Active Directory.", alias="domainName")
    machine_accounts: Optional[Annotated[List[McmMachineAccount], Field(min_length=1)]] = Field(description="Specifies a list of computer names used to identify the Cohesity Cluster on the Active Directory domain. The first machine account is used as primary machine account and it can not be modified.", alias="machineAccounts")
    organizational_unit_name: Optional[StrictStr] = Field(default=None, description="Specifies an optional organizational unit name.", alias="organizationalUnitName")
    preferred_domain_controllers: Optional[List[DomainController]] = Field(default=None, description="Specifies a list of preferred domain controllers of this Active Directory.", alias="preferredDomainControllers")
    trusted_domain_params: Optional[TrustedDomainParams] = Field(default=None, description="Specifies the params of trusted domain info of an Active Directory.", alias="trustedDomainParams")
    work_group_name: Optional[StrictStr] = Field(default=None, description="Specifies a work group name.", alias="workGroupName")
    admin_params: Optional[Dict[str, Any]] = Field(description="Specifies the params of a user with administrative privilege of this Active Directory.", alias="adminParams")
    overwrite_machine_accounts: Optional[StrictBool] = Field(default=None, description="Specifies if specified machine accounts should overwrite existing machine accounts.", alias="overwriteMachineAccounts")
    trusted_domain_list: Optional[List[TrustedDomainInfo]] = Field(default=None, description="A list of domains which this domain trusts.", alias="trustedDomainList")
    __properties: ClassVar[List[str]] = ["domainName", "machineAccounts", "organizationalUnitName", "preferredDomainControllers", "trustedDomainParams", "workGroupName", "adminParams", "overwriteMachineAccounts", "trustedDomainList"]

    @field_validator('domain_name')
    def domain_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$", value):
            raise ValueError(r"must validate the regular expression /^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])(\.([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]{0,61}[a-zA-Z0-9]))*$/")
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
        """Create an instance of CreateOrUpdateActiveDirectoryRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in trusted_domain_list (list)
        _items = []
        if self.trusted_domain_list:
            for _item_trusted_domain_list in self.trusted_domain_list:
                if _item_trusted_domain_list:
                    _items.append(_item_trusted_domain_list.to_dict())
            _dict['trustedDomainList'] = _items
        # set to None if domain_name (nullable) is None
        # and model_fields_set contains the field
        if self.domain_name is None and "domain_name" in self.model_fields_set:
            _dict['domainName'] = None

        # set to None if machine_accounts (nullable) is None
        # and model_fields_set contains the field
        if self.machine_accounts is None and "machine_accounts" in self.model_fields_set:
            _dict['machineAccounts'] = None

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

        # set to None if admin_params (nullable) is None
        # and model_fields_set contains the field
        if self.admin_params is None and "admin_params" in self.model_fields_set:
            _dict['adminParams'] = None

        # set to None if overwrite_machine_accounts (nullable) is None
        # and model_fields_set contains the field
        if self.overwrite_machine_accounts is None and "overwrite_machine_accounts" in self.model_fields_set:
            _dict['overwriteMachineAccounts'] = None

        # set to None if trusted_domain_list (nullable) is None
        # and model_fields_set contains the field
        if self.trusted_domain_list is None and "trusted_domain_list" in self.model_fields_set:
            _dict['trustedDomainList'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrUpdateActiveDirectoryRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domainName": obj.get("domainName"),
            "machineAccounts": [McmMachineAccount.from_dict(_item) for _item in obj["machineAccounts"]] if obj.get("machineAccounts") is not None else None,
            "organizationalUnitName": obj.get("organizationalUnitName"),
            "preferredDomainControllers": [DomainController.from_dict(_item) for _item in obj["preferredDomainControllers"]] if obj.get("preferredDomainControllers") is not None else None,
            "trustedDomainParams": TrustedDomainParams.from_dict(obj["trustedDomainParams"]) if obj.get("trustedDomainParams") is not None else None,
            "workGroupName": obj.get("workGroupName"),
            "adminParams": obj.get("adminParams"),
            "overwriteMachineAccounts": obj.get("overwriteMachineAccounts"),
            "trustedDomainList": [TrustedDomainInfo.from_dict(_item) for _item in obj["trustedDomainList"]] if obj.get("trustedDomainList") is not None else None
        })
        return _obj


