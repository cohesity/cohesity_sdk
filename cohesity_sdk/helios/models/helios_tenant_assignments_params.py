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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class HeliosTenantAssignmentsParams(BaseModel):
    """
    Parameters to be specified for assigning properties like policies to a tenant.
    """ # noqa: E501
    cluster_identifier: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Specifies the the cluster on which properties are to be assigned. The format is clusterId:clusterIncarnationId.", alias="clusterIdentifier")
    policy_ids: Optional[List[StrictStr]] = Field(default=None, description="List of policies on the cluster, to be assigned to the Tenant.", alias="policyIds")
    __properties: ClassVar[List[str]] = ["clusterIdentifier", "policyIds"]

    @field_validator('cluster_identifier')
    def cluster_identifier_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([0-9]+:[0-9]+)$", value):
            raise ValueError(r"must validate the regular expression /^([0-9]+:[0-9]+)$/")
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
        """Create an instance of HeliosTenantAssignmentsParams from a JSON string"""
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
        # set to None if cluster_identifier (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_identifier is None and "cluster_identifier" in self.model_fields_set:
            _dict['clusterIdentifier'] = None

        # set to None if policy_ids (nullable) is None
        # and model_fields_set contains the field
        if self.policy_ids is None and "policy_ids" in self.model_fields_set:
            _dict['policyIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosTenantAssignmentsParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterIdentifier": obj.get("clusterIdentifier"),
            "policyIds": obj.get("policyIds")
        })
        return _obj


