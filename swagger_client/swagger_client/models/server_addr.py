# coding: utf-8

"""
    Balancer

    Simple iperf load balancer  # noqa: E501

    OpenAPI spec version: 0.1.0

    Contact: vinogradov.alek@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ServerAddr(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ip': 'str',
        'port': 'int',
        'port_iperf': 'int',
    }

    attribute_map = {
        'ip': 'ip',
        'port': 'port',
        'port_iperf': 'port_iperf',
        'time': 'time'
    }

    def __init__(self, ip=None, port=None, port_iperf=None, time=None):  # noqa: E501
        """ServerAddr - a model defined in Swagger"""  # noqa: E501
        self._ip = None
        self._port = None
        self._port_iperf = None
        self._time = None
        self.discriminator = None
        if ip is not None:
            self.ip = ip
        self.port = port
        self.port_iperf = port_iperf

        if time is not None:
            self.time = time

    @property
    def ip(self):
        """Gets the ip of this ServerAddr.  # noqa: E501


        :return: The ip of this ServerAddr.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ServerAddr.


        :param ip: The ip of this ServerAddr.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def port(self):
        """Gets the port of this ServerAddr.  # noqa: E501

        port of Service server  # noqa: E501


        :return: The port of this ServerAddr.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ServerAddr.

        port of Service server  # noqa: E501


        :param port: The port of this ServerAddr.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def port_iperf(self):
        """Gets the port_iperf of this ServerAddr.  # noqa: E501

        port of iperf server  # noqa: E501

        :return: The port_iperf of this ServerAddr.  # noqa: E501
        :rtype: int
        """
        return self._port_iperf

    @port_iperf.setter
    def port_iperf(self, port_iperf):
        """Sets the port_iperf of this ServerAddr.

        port of iperf server  # noqa: E501

        :param port_iperf: The port_iperf of this ServerAddr.  # noqa: E501
        :type: int
        """
        if port_iperf is None:
            raise ValueError("Invalid value for `port_iperf`, must not be `None`")  # noqa: E501

        self._port_iperf = port_iperf

    @property
    def time(self):
        """Gets the time of this ServerAddr.  # noqa: E501


        :return: The time of this ServerAddr.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ServerAddr.


        :param time: The time of this ServerAddr.  # noqa: E501
        :type: datetime
        """

        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ServerAddr, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerAddr):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
