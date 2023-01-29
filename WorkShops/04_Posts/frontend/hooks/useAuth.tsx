import React, { useState } from "react";
import { RegisterType, ErrorType, LoginType } from "../types";
import axios from "axios";
import { REGISTER_URL, LOGIN_URL } from "../constant/urls";
import { useRouter } from "next/router";

const useAuth = () => {
  const [errorMessage, setErrorMessage] = useState<ErrorType | null>(null);
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const registerFunc = async (registerInfo: RegisterType) => {
    setLoading(true);
    try {
      const { data } = await axios.post(REGISTER_URL, registerInfo);
      // console.log(data);
      setErrorMessage(null);
      sessionStorage.setItem("user", JSON.stringify(data));
      router.push("/");
    } catch (error: any) {
      setErrorMessage(error.response.data);
    }
    setLoading(false);
  };

  const loginFunc = async (loginInfo: LoginType) => {
    setLoading(true);
    try {
      const { data } = await axios.post(LOGIN_URL, loginInfo);
      setErrorMessage(null);
      sessionStorage.setItem("user", JSON.stringify(data));
      router.push("/");
    } catch (error: any) {
      setErrorMessage(error.response.data);
    }
    setLoading(false);
  };

  return { registerFunc, errorMessage, loading, loginFunc };
};

export default useAuth;
