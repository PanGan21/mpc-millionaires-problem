/* Generated by Yosys 0.39 (git sha1 00338082b00, clang++ 14.0.0 -fPIC -Os) */

module test(x_0, x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, x_10, x_11, x_12, x_13, x_14, x_15, x_16, x_17, x_18, x_19, x_20
, x_21, x_22, x_23, x_24, x_25, x_26, x_27, x_28, x_29, x_30, x_31, y_0, y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_8, y_9
, y_10, y_11, y_12, y_13, y_14, y_15, y_16, y_17, y_18, y_19, y_20, y_21, y_22, y_23, y_24, y_25, y_26, y_27, y_28, y_29, y_30
, y_31, out);
  wire _000_;
  wire _001_;
  wire _002_;
  wire _003_;
  wire _004_;
  wire _005_;
  wire _006_;
  wire _007_;
  wire _008_;
  wire _009_;
  wire _010_;
  wire _011_;
  wire _012_;
  wire _013_;
  wire _014_;
  wire _015_;
  wire _016_;
  wire _017_;
  wire _018_;
  wire _019_;
  wire _020_;
  wire _021_;
  wire _022_;
  wire _023_;
  wire _024_;
  wire _025_;
  wire _026_;
  wire _027_;
  wire _028_;
  wire _029_;
  wire _030_;
  wire _031_;
  wire _032_;
  wire _033_;
  wire _034_;
  wire _035_;
  wire _036_;
  wire _037_;
  wire _038_;
  wire _039_;
  wire _040_;
  wire _041_;
  wire _042_;
  wire _043_;
  wire _044_;
  wire _045_;
  wire _046_;
  wire _047_;
  wire _048_;
  wire _049_;
  wire _050_;
  wire _051_;
  wire _052_;
  wire _053_;
  wire _054_;
  wire _055_;
  wire _056_;
  wire _057_;
  wire _058_;
  wire _059_;
  wire _060_;
  wire _061_;
  output out;
  wire out;
  input x_0;
  wire x_0;
  input x_1;
  wire x_1;
  input x_10;
  wire x_10;
  input x_11;
  wire x_11;
  input x_12;
  wire x_12;
  input x_13;
  wire x_13;
  input x_14;
  wire x_14;
  input x_15;
  wire x_15;
  input x_16;
  wire x_16;
  input x_17;
  wire x_17;
  input x_18;
  wire x_18;
  input x_19;
  wire x_19;
  input x_2;
  wire x_2;
  input x_20;
  wire x_20;
  input x_21;
  wire x_21;
  input x_22;
  wire x_22;
  input x_23;
  wire x_23;
  input x_24;
  wire x_24;
  input x_25;
  wire x_25;
  input x_26;
  wire x_26;
  input x_27;
  wire x_27;
  input x_28;
  wire x_28;
  input x_29;
  wire x_29;
  input x_3;
  wire x_3;
  input x_30;
  wire x_30;
  input x_31;
  wire x_31;
  input x_4;
  wire x_4;
  input x_5;
  wire x_5;
  input x_6;
  wire x_6;
  input x_7;
  wire x_7;
  input x_8;
  wire x_8;
  input x_9;
  wire x_9;
  input y_0;
  wire y_0;
  input y_1;
  wire y_1;
  input y_10;
  wire y_10;
  input y_11;
  wire y_11;
  input y_12;
  wire y_12;
  input y_13;
  wire y_13;
  input y_14;
  wire y_14;
  input y_15;
  wire y_15;
  input y_16;
  wire y_16;
  input y_17;
  wire y_17;
  input y_18;
  wire y_18;
  input y_19;
  wire y_19;
  input y_2;
  wire y_2;
  input y_20;
  wire y_20;
  input y_21;
  wire y_21;
  input y_22;
  wire y_22;
  input y_23;
  wire y_23;
  input y_24;
  wire y_24;
  input y_25;
  wire y_25;
  input y_26;
  wire y_26;
  input y_27;
  wire y_27;
  input y_28;
  wire y_28;
  input y_29;
  wire y_29;
  input y_3;
  wire y_3;
  input y_30;
  wire y_30;
  input y_31;
  wire y_31;
  input y_4;
  wire y_4;
  input y_5;
  wire y_5;
  input y_6;
  wire y_6;
  input y_7;
  wire y_7;
  input y_8;
  wire y_8;
  input y_9;
  wire y_9;
  assign _028_ = ~(x_21 | x_20);
  assign _029_ = ~(x_23 | x_22);
  assign _030_ = _028_ & _029_;
  assign _031_ = ~(x_17 | x_16);
  assign _032_ = ~(x_19 | x_18);
  assign _033_ = _031_ & _032_;
  assign _034_ = _030_ & _033_;
  assign _035_ = ~(x_29 | x_28);
  assign _036_ = ~(x_31 | x_30);
  assign _037_ = _035_ & _036_;
  assign _038_ = ~(x_25 | x_24);
  assign _039_ = ~(x_27 | x_26);
  assign _040_ = _038_ & _039_;
  assign _041_ = _037_ & _040_;
  assign _042_ = _034_ & _041_;
  assign _043_ = x_5 & ~(x_4);
  assign _044_ = ~(x_7 | x_6);
  assign _045_ = _043_ & _044_;
  assign _046_ = x_0 & ~(x_1);
  assign _047_ = x_3 & ~(x_2);
  assign _048_ = _046_ & _047_;
  assign _049_ = _045_ & _048_;
  assign _050_ = x_13 & ~(x_12);
  assign _051_ = ~(x_15 | x_14);
  assign _052_ = _050_ & _051_;
  assign _053_ = x_9 & x_8;
  assign _054_ = ~(x_11 | x_10);
  assign _055_ = _053_ & _054_;
  assign _056_ = _052_ & _055_;
  assign _057_ = _049_ & _056_;
  assign _058_ = _042_ & _057_;
  assign _059_ = ~(y_21 | y_20);
  assign _060_ = ~(y_23 | y_22);
  assign _061_ = _059_ & _060_;
  assign _000_ = ~(y_17 | y_16);
  assign _001_ = ~(y_19 | y_18);
  assign _002_ = _000_ & _001_;
  assign _003_ = _061_ & _002_;
  assign _004_ = ~(y_29 | y_28);
  assign _005_ = ~(y_31 | y_30);
  assign _006_ = _004_ & _005_;
  assign _007_ = ~(y_25 | y_24);
  assign _008_ = ~(y_27 | y_26);
  assign _009_ = _007_ & _008_;
  assign _010_ = _006_ & _009_;
  assign _011_ = _003_ & _010_;
  assign _012_ = y_5 & y_4;
  assign _013_ = ~(y_7 | y_6);
  assign _014_ = _012_ & _013_;
  assign _015_ = y_0 & ~(y_1);
  assign _016_ = y_3 & ~(y_2);
  assign _017_ = _015_ & _016_;
  assign _018_ = _014_ & _017_;
  assign _019_ = ~(y_13 | y_12);
  assign _020_ = ~(y_15 | y_14);
  assign _021_ = _019_ & _020_;
  assign _022_ = y_8 & ~(y_9);
  assign _023_ = y_10 & ~(y_11);
  assign _024_ = _022_ & _023_;
  assign _025_ = _021_ & _024_;
  assign _026_ = _018_ & _025_;
  assign _027_ = _011_ & _026_;
  assign out = _058_ & _027_;
endmodule