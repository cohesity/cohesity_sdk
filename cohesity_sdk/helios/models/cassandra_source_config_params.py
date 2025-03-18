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
from cohesity_sdk.helios.models.cassandra_port_info import CassandraPortInfo
from cohesity_sdk.helios.models.cassandra_security_info import CassandraSecurityInfo
from typing import Set
from typing_extensions import Self

class CassandraSourceConfigParams(BaseModel):
    """
    Specifies the parameters fetched by reading cassandra configuration on the seed node.
    """ # noqa: E501
    cassandra_partitioner: Optional[StrictStr] = Field(default=None, description="Cassandra partitioner required in compaction.", alias="cassandraPartitioner")
    cassandra_port_info: Optional[CassandraPortInfo] = Field(default=None, alias="cassandraPortInfo")
    cassandra_security_info: Optional[CassandraSecurityInfo] = Field(default=None, alias="cassandraSecurityInfo")
    cassandra_version: Optional[StrictStr] = Field(default=None, description="Cassandra Version.", alias="cassandraVersion")
    commit_log_backup_location: Optional[StrictStr] = Field(default=None, description="Commit Logs backup location on cassandra nodes", alias="commitLogBackupLocation")
    data_center_names: Optional[List[StrictStr]] = Field(default=None, description="Data centers for this cluster.", alias="dataCenterNames")
    dse_version: Optional[StrictStr] = Field(default=None, description="DSE Version", alias="dseVersion")
    endpoint_snitch: Optional[StrictStr] = Field(default=None, description="Endpoint snitch used for this cluster.", alias="endpointSnitch")
    is_jmx_auth_enable: Optional[StrictBool] = Field(default=None, description="Is JMX Authentication enabled in this cluster ?", alias="isJmxAuthEnable")
    kerberos_sasl_protocol: Optional[StrictStr] = Field(default=None, description="Populated if cassandraAuthType is Kerberos.", alias="kerberosSaslProtocol")
    seeds: Optional[List[StrictStr]] = Field(default=None, description="Seed nodes of this cluster.")
    __properties: ClassVar[List[str]] = ["cassandraPartitioner", "cassandraPortInfo", "cassandraSecurityInfo", "cassandraVersion", "commitLogBackupLocation", "dataCenterNames", "dseVersion", "endpointSnitch", "isJmxAuthEnable", "kerberosSaslProtocol", "seeds"]

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
        """Create an instance of CassandraSourceConfigParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cassandra_port_info
        if self.cassandra_port_info:
            _dict['cassandraPortInfo'] = self.cassandra_port_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cassandra_security_info
        if self.cassandra_security_info:
            _dict['cassandraSecurityInfo'] = self.cassandra_security_info.to_dict()
        # set to None if cassandra_partitioner (nullable) is None
        # and model_fields_set contains the field
        if self.cassandra_partitioner is None and "cassandra_partitioner" in self.model_fields_set:
            _dict['cassandraPartitioner'] = None

        # set to None if cassandra_version (nullable) is None
        # and model_fields_set contains the field
        if self.cassandra_version is None and "cassandra_version" in self.model_fields_set:
            _dict['cassandraVersion'] = None

        # set to None if commit_log_backup_location (nullable) is None
        # and model_fields_set contains the field
        if self.commit_log_backup_location is None and "commit_log_backup_location" in self.model_fields_set:
            _dict['commitLogBackupLocation'] = None

        # set to None if dse_version (nullable) is None
        # and model_fields_set contains the field
        if self.dse_version is None and "dse_version" in self.model_fields_set:
            _dict['dseVersion'] = None

        # set to None if endpoint_snitch (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint_snitch is None and "endpoint_snitch" in self.model_fields_set:
            _dict['endpointSnitch'] = None

        # set to None if is_jmx_auth_enable (nullable) is None
        # and model_fields_set contains the field
        if self.is_jmx_auth_enable is None and "is_jmx_auth_enable" in self.model_fields_set:
            _dict['isJmxAuthEnable'] = None

        # set to None if kerberos_sasl_protocol (nullable) is None
        # and model_fields_set contains the field
        if self.kerberos_sasl_protocol is None and "kerberos_sasl_protocol" in self.model_fields_set:
            _dict['kerberosSaslProtocol'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CassandraSourceConfigParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cassandraPartitioner": obj.get("cassandraPartitioner"),
            "cassandraPortInfo": CassandraPortInfo.from_dict(obj["cassandraPortInfo"]) if obj.get("cassandraPortInfo") is not None else None,
            "cassandraSecurityInfo": CassandraSecurityInfo.from_dict(obj["cassandraSecurityInfo"]) if obj.get("cassandraSecurityInfo") is not None else None,
            "cassandraVersion": obj.get("cassandraVersion"),
            "commitLogBackupLocation": obj.get("commitLogBackupLocation"),
            "dataCenterNames": obj.get("dataCenterNames"),
            "dseVersion": obj.get("dseVersion"),
            "endpointSnitch": obj.get("endpointSnitch"),
            "isJmxAuthEnable": obj.get("isJmxAuthEnable"),
            "kerberosSaslProtocol": obj.get("kerberosSaslProtocol"),
            "seeds": obj.get("seeds")
        })
        return _obj


