module test(x, y, out);
    input [31:0] x;
    input [31:0] y;
    output out;

    reg [31:0] tmp;
    initial begin
        out = (x == 9001) && (y == 1337);
    end
endmodule