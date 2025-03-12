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
from cohesity_sdk.helios.models.quota_policy import QuotaPolicy
from cohesity_sdk.helios.models.user_quota import UserQuota
from typing import Optional, Set
from typing_extensions import Self

class ViewUserQuotas(BaseModel):
    """
    Specifies the default logical user quota on the View along with the list of logical quota overrides for each user.
    """ # noqa: E501
    default_quota_policy: Optional[QuotaPolicy] = Field(default=None, alias="defaultQuotaPolicy")
    enabled: StrictBool = Field(description="Specifies whether user quota is enabled for the View.")
    cookie: Optional[StrictStr] = Field(default=None, description="Specifies the pagination cookie.")
    override_existing_per_user_quotas: Optional[StrictBool] = Field(default=None, description="By default, the overrides specified in userQuotas is treated as delta and the existing overrides will be left untouched. Set this to true, if the existing overrides should be cleared before applying overrides specified in userQuotas.", alias="overrideExistingPerUserQuotas")
    user_quotas: Optional[List[UserQuota]] = Field(description="Array of UserQuota. Specifies the list of UserQuota for each user.", alias="userQuotas")
    __properties: ClassVar[List[str]] = ["defaultQuotaPolicy", "enabled", "cookie", "overrideExistingPerUserQuotas", "userQuotas"]

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
        """Create an instance of ViewUserQuotas from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of default_quota_policy
        if self.default_quota_policy:
            _dict['defaultQuotaPolicy'] = self.default_quota_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in user_quotas (list)
        _items = []
        if self.user_quotas:
            for _item_user_quotas in self.user_quotas:
                if _item_user_quotas:
                    _items.append(_item_user_quotas.to_dict())
            _dict['userQuotas'] = _items
        # set to None if cookie (nullable) is None
        # and model_fields_set contains the field
        if self.cookie is None and "cookie" in self.model_fields_set:
            _dict['cookie'] = None

        # set to None if override_existing_per_user_quotas (nullable) is None
        # and model_fields_set contains the field
        if self.override_existing_per_user_quotas is None and "override_existing_per_user_quotas" in self.model_fields_set:
            _dict['overrideExistingPerUserQuotas'] = None

        # set to None if user_quotas (nullable) is None
        # and model_fields_set contains the field
        if self.user_quotas is None and "user_quotas" in self.model_fields_set:
            _dict['userQuotas'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ViewUserQuotas from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "defaultQuotaPolicy": QuotaPolicy.from_dict(obj["defaultQuotaPolicy"]) if obj.get("defaultQuotaPolicy") is not None else None,
            "enabled": obj.get("enabled"),
            "cookie": obj.get("cookie"),
            "overrideExistingPerUserQuotas": obj.get("overrideExistingPerUserQuotas"),
            "userQuotas": [UserQuota.from_dict(_item) for _item in obj["userQuotas"]] if obj.get("userQuotas") is not None else None
        })
        return _obj


