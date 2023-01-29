import Head from "next/head";
import React, { useState } from "react";
import { useForm, SubmitHandler } from "react-hook-form";
import Loader from "../components/Loader";
import useAuth from "../hooks/useAuth";
import { LoginType, RegisterType } from "../types";
import { motion } from "framer-motion";

type Props = {};

const login = (props: Props) => {
  const { loginFunc, errorMessage, loading } = useAuth();
  // useForm --> form doğrulama için
  console.log(errorMessage);
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginType>();

  // https://react-hook-form.com/get-started/
  // onSubmit'i neden oluşturduk. Yukardaki link'den ulaşılabilir.
  const onSubmit: SubmitHandler<LoginType> = async (data) => {
    await loginFunc(data);
  };

  return (
    <div>
      <Head>
        <title>Login</title>
      </Head>

      <motion.div
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        className="flex justify-center items-center h-screen"
      >
        <form
          className=" flex flex-col gap-10"
          onSubmit={handleSubmit(onSubmit)}
        >
          <div className="inputDiv">
            <input
              type="text"
              placeholder="Username"
              className="registerInput"
              {...register("username", { required: true })}
            />
          </div>
          <div className="inputDiv">
            <input
              type="text"
              placeholder="Password"
              className="registerInput"
              {...register("password", { required: true })}
            />
            {errorMessage?.non_field_errors && (
              <p className="errorMessage">
                * {errorMessage.non_field_errors[0]}
              </p>
            )}
          </div>
          <button type="submit" className="submitButton">
            {loading ? <Loader color="#bcc" /> : "Login"}
          </button>
        </form>
      </motion.div>
    </div>
  );
};

export default login;
