import React, { useState } from "react";
import { RegisterType, ErrorType } from "../types";
import axios from "axios";
import { REGISTER_URL } from "../constant/urls";

const useAuth = () => {
  const [errorMessage, setErrorMessage] = useState<ErrorType>();
  const registerFunc = async (registerInfo: RegisterType) => {
    try {
      const { data } = await axios.post(REGISTER_URL, registerInfo);
      // console.log(data);
    } catch (error: any) {
      setErrorMessage(error.response.data);
      console.log(error);
    }
  };

  return { registerFunc, errorMessage };
};

export default useAuth;
