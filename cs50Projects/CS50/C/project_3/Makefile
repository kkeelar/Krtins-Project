CC=clang
CFLAGS=-g -Wall


BIN=downloadex


all: $(BIN)


%: %.c
	$(CC) $(CFLAGS) $< -o $@ -lcurl -lcs50




clean:
	$(RM) -rf $(BIN) *.dSYM