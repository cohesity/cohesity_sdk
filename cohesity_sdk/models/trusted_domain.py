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
from cohesity_sdk.models.domain_controller import DomainController
from typing import Optional, Set
from typing_extensions import Self

class TrustedDomain(BaseModel):
    """
    Specifies the details of a trusted domain.
    """ # noqa: E501
    domain_controllers_deny_list: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Specifies a list of denied domain controllers of this domain.", alias="domainControllersDenyList")
    domain_name: Optional[StrictStr] = Field(default=None, description="Specifies a domain name.", alias="domainName")
    preferred_domain_controllers: Optional[List[DomainController]] = Field(default=None, description="Specifies a list of preferred domain controllers for this domain.", alias="preferredDomainControllers")
    __properties: ClassVar[List[str]] = ["domainControllersDenyList", "domainName", "preferredDomainControllers"]

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
        """Create an instance of TrustedDomain from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in preferred_domain_controllers (list)
        _items = []
        if self.preferred_domain_controllers:
            for _item_preferred_domain_controllers in self.preferred_domain_controllers:
                if _item_preferred_domain_controllers:
                    _items.append(_item_preferred_domain_controllers.to_dict())
            _dict['preferredDomainControllers'] = _items
        # set to None if domain_name (nullable) is None
        # and model_fields_set contains the field
        if self.domain_name is None and "domain_name" in self.model_fields_set:
            _dict['domainName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrustedDomain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domainControllersDenyList": obj.get("domainControllersDenyList"),
            "domainName": obj.get("domainName"),
            "preferredDomainControllers": [DomainController.from_dict(_item) for _item in obj["preferredDomainControllers"]] if obj.get("preferredDomainControllers") is not None else None
        })
        return _obj


